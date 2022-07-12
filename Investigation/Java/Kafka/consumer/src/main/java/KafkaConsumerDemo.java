import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

/**
 * @author jiaqi.zhang
 * @version 1.0
 * @date 2022/7/11
 */
public class KafkaConsumerDemo {
  static Logger logger = LoggerFactory.getLogger(KafkaConsumerDemo.class);
  public static void main(String[] args) {
    Properties prop = new Properties();
    //kafka连接地址
    prop.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, KafkaProperties.KAFKA_SERVER_URL + ":" + KafkaProperties.KAFKA_SERVER_PORT);
    prop.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
    prop.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
    prop.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true");
    //自动提交偏移量周期
    prop.put(ConsumerConfig.AUTO_COMMIT_INTERVAL_MS_CONFIG, "1000");
    //earliest：拉取最早的数据
    //latest：拉取最新的数据
    //none：报错
    prop.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
    //一个消费者组里只有一个消费者
    prop.put(ConsumerConfig.GROUP_ID_CONFIG, "test-consumer-group");
    //创建kafka消费者对象
    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(prop);
    //设置自动分配topic与消费者对象
    consumer.subscribe(Collections.singleton(KafkaProperties.TOPIC));
    while (true) {
      //消费数据, 一次10条
      ConsumerRecords<String, String> poll = consumer.poll(Duration.ofMillis(0));
      //遍历输出
      for (ConsumerRecord<String, String> record : poll) {
        System.out.println(record.offset() + "\t" + record.key() + "\t" + record.value());
      }
    }
  }
}
