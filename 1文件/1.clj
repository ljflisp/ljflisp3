;(println "hello world")
(do
  (println "What's your language?")
  (let[name (read-line)]
    (println(str "Hey, " name))))