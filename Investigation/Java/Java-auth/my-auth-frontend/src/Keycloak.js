import Keycloak from "keycloak-js";
import { config } from "./Constants";

const keycloak = new Keycloak({
  url: config.url.KEYCLOAK_BASE_URL,
  realm: "automl_dev",
  clientId: "automl_public_client",
});

export default keycloak;