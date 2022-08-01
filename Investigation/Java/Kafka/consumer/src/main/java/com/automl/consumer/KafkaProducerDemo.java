package com.automl.consumer;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

/**
 * @author jiaqi.zhang
 * @version 1.0
 * {@code @date} 2022/7/11
 */
public class KafkaProducerDemo {
    //  public static final Logger logger = LogManager.getLogger();

    public static void main(String[] args) {
        // 创建配置
        Properties prop = new Properties();

        // kafka连接地址
        prop.put(
            ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
            KafkaProperties.KAFKA_SERVER_URL + ":" + KafkaProperties.KAFKA_SERVER_PORT);
        // 用于实现Serializer接口的密钥的串行器类。
        prop.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        prop.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        // 生产者数据安全
        prop.put(ProducerConfig.ACKS_CONFIG, "1");

        // 创建生产者
        KafkaProducer<String, String> producer = new KafkaProducer<>(prop);

        for (int i = 0; i < 10; i++) {
            System.out.println("开始发送");
            // 创建消息
            ProducerRecord<String, String> producerRecord =
                new ProducerRecord<>(KafkaProperties.TOPIC, "hello world" + i);
            // 发送消息
            producer.send(producerRecord);
            try {
                // 每条消息间隔100毫秒
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("发送结束");
        }
        System.out.println("game over!!!");
    }
}
