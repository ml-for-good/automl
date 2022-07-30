package com.automl.config;

import java.util.Collections;

import javax.servlet.http.HttpServletRequest;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationConverter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;

@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(securedEnabled = true, jsr250Enabled = true, prePostEnabled = true)
public class ProjectSecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(new KeycloakRoleConverter());

        // enable CORS
        http.cors().configurationSource(new CorsConfigurationSource() {
                @Override
                public CorsConfiguration getCorsConfiguration(HttpServletRequest request) {
                    CorsConfiguration config = new CorsConfiguration();
                    config.setAllowedOrigins(Collections.singletonList("http://localhost:4200"));
                    config.setAllowedMethods(Collections.singletonList("*"));
                    config.setAllowCredentials(true);
                    config.setAllowedHeaders(Collections.singletonList("*"));
                    config.setMaxAge(3600L);
                    return config;
                }
            }).and()
            .authorizeRequests()
            .antMatchers("/dashboard").hasAnyRole("USER")
            .antMatchers("/hello").permitAll()
            .antMatchers("/sample").authenticated()
            .and().csrf().disable() // no need of csrf token because we are using oauth 2.0
            .oauth2ResourceServer().jwt().jwtAuthenticationConverter(jwtAuthenticationConverter); // we are using jwt for oauth 2.0

        /**
         * This configuration is needed to view the /h2-console without any issues.
         * Since H2 Console uses frames to display the UI, we need to allow the frames.
         * Otherwise since by default Spring Security consider X-Frame-Options: DENY
         * to avoid Clickjacking attacks, the /h2-console will not work properly.
         * More details can be found at
         * https://docs.spring.io/spring-security/site/docs/5.0.x/reference/html/headers.html#headers-frame-options
         */
        http.headers().frameOptions().sameOrigin();

    }
}
