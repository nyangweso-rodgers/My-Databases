// controllers

import producer from "../Kafka-Producer-Service/test-producer.js";

export const postMessage = async (req, res) => {
  try {
    console.log("reg", req);
    const message = req.body.message;
    const payloads = [{ topic: "test-topic",  messages: message, key: "test-key"}];

    producer.send(payloads, (error, data) => {
      if (error) {
        console.error("Error sending message:", error);
        res.status(500).json({ error: "Error sending message to Kafka" });
      } else {
        console.log("Message sent successfully:", data);
        res.status(200).json({ message: "Message sent successfully" });
      }
    });
  } catch (error) {
    console.log("Error sending message:", error);
    res.status(500).json({ error: "Error sending message to Kafka" });
  }
};