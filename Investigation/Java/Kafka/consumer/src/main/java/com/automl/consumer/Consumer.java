package com.automl.consumer;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

/**
 * @author jiaqi.zhang
 * @version 1.0
 * {@code @date} 2022/7/7
 */
public class Consumer {
    private final String kafkaHost;
    private final String topic;
    private final String groupId;

    public Consumer(String kafkaHost, String topic, String groupId) {
        this.kafkaHost = kafkaHost;
        this.topic = topic;
        this.groupId = groupId;
    }

    public ConsumerRecords<String, String> configConsumer() {
        Properties properties = new Properties();
        // kafka连接地址
        properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaHost);
        properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        properties.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true");
        // 自动提交偏移量周期
        properties.put(ConsumerConfig.AUTO_COMMIT_INTERVAL_MS_CONFIG, "1000");
        // earliest：拉取最早的数据
        properties.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        // 一个消费者组里只有一个消费者
        properties.put(ConsumerConfig.GROUP_ID_CONFIG, groupId);
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);
        consumer.subscribe(Collections.singleton(topic));
        return consumer.poll(Duration.ofMillis(1000));
    }
}
