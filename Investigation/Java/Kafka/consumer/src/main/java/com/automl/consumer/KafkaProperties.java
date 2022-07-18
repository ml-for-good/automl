package com.automl.consumer;

/**
 * @author jiaqi.zhang
 * @version 1.0
 * {@code @date} 2022/7/11
 */
public class KafkaProperties {
  public static final String TOPIC = "automl";
  public static final String KAFKA_SERVER_URL = "localhost";
  public static final int KAFKA_SERVER_PORT = 9092;

  public static final String KAFKA_GROUP_ID = "";

  private KafkaProperties() {}
}
