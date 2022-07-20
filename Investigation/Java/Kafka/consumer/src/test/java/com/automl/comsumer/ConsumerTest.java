package com.automl.comsumer;

import com.automl.consumer.Consumer;
import com.automl.consumer.KafkaProperties;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.junit.jupiter.api.Test;

/**
 * @author jiaqi.zhang
 * @version 1.0 {@code @date} 2022/7/18
 */
public class ConsumerTest {
  @Test
  public void simpleConsumerTest() {
    Consumer consumer =
        new Consumer(
            KafkaProperties.KAFKA_SERVER_URL + ":" + KafkaProperties.KAFKA_SERVER_PORT,
            KafkaProperties.TOPIC,
            KafkaProperties.KAFKA_GROUP_ID);
    for (ConsumerRecord<String, String> consumerRecord : consumer.configConsumer()) {
      System.out.println(
          KafkaProperties.KAFKA_GROUP_ID
              + " received message : from partition "
              + consumerRecord.partition()
              + ", ("
              + consumerRecord.key()
              + ", "
              + consumerRecord.value()
              + ") at offset "
              + consumerRecord.offset());
    }
  }
}
