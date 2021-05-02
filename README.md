# Spark_And_Hadoop_Mapreduce
## Spark
### Tổng quan 
Apache Spark là một open source cluster computing framework được phát triển sơ khởi vào năm 2009 bởi AMPLab tại đại học California. Nó cho phép xây dựng các mô hình dự đoán nhanh chóng với việc tính toán được thực hiện trên một nhóm các máy tính, có có thể tính toán cùng lúc trên toàn bộ tập dữ liệu mà không cần phải trích xuất mẫu tính toán thử nghiệm. Tốc độ xử lý của Spark có được do việc tính toán được thực hiện cùng lúc trên nhiều máy khác nhau. Đồng thời việc tính toán được thực hiện ở bộ nhớ trong (in-memories) hay thực hiện hoàn toàn trên RAM.
### Cấu trúc
Thành phần trung của Spark là Spark Core: cung cấp những chức năng cơ bản nhất của Spark như lập lịch cho các tác vụ, quản lý bộ nhớ, fault recovery, tương tác với các hệ thống lưu trữ…Đặc biệt, Spark Core cung cấp API để định nghĩa RDD (Resilient Distributed DataSet) là tập hợp của các item được phân tán trên các node của cluster và có thể được xử lý song song

Spark có thể chạy trên nhiều loại Cluster Managers như Hadoop YARN, Apache Mesos hoặc trên chính cluster manager được cung cấp bởi Spark được gọi là Standalone Scheduler.

-	Spark SQL cho phép truy vấn dữ liệu cấu trúc qua các câu lệnh SQL. Spark SQL có thể thao tác với nhiều nguồn dữ liệu như Hive tables, Parquet, và JSON.
-	Spark Streaming cung cấp API để dễ dàng xử lý dữ liệu stream
- MLlib Cung cấp rất nhiều thuật toán của học máy như: classification, regression, clustering, collaborative filtering…
- GraphX là thư viện để xử lý đồ thị.
### Quản lý bộ nhớ
Spark giải quyết các vấn đề vấn đề xung quanh định nghĩa Resilient Distributed Datasets (RDDs). RDDs hỗ trợ hai kiểu thao tác thao tác: transformations và action. Thao tác chuyển đổi(tranformation) tạo ra dataset từ dữ liệu có sẵn. Thao tác actions trả về giá trị cho chương trình điều khiển (driver program) sau khi thực hiện tính toán trên dataset.

Spark thực hiện đưa các thao tác RDD chuyển đổi vào DAG (Directed Acyclic Graph) và bắt đầu thực hiện. Khi một action được gọi trên RDD, Spark sẽ tạo DAG và chuyển cho DAG scheduler. DAG scheduler chia các thao tác thành các nhóm (stage) khác nhau của các task. Mỗi Stage bao gồm các task dựa trên phân vùng của dữ liệu đầu vào có thể pipline với nhau và có thể thực hiện một cách độc lập trên một máy worker. DAG scheduler sắp xếp các thao tác phù hợp với quá trình thực hiện theo thời gian sao cho tối ưu nhất.

Mỗi Worker bao gồm một hoặc nhiều Excuter. Các excuter chịu trách nhiệm thực hiện các task trên các luồng riêng biệt. Việc chia nhỏ các task giúp đem lại hiệu năng cao hơn, giảm thiểu ảnh hưởng của dữ liệu không đối xứng (kích thước các file không đồng đều).
## Hadoop_Mapreduce
### MapReduce là gì?
MapReduce được thiết kế bởi Google như 1 mô hình lập trình xử lý tập dữ liệu lớn song song, thuật toán được phân tán trên 1 cụm. Mặc dù, MapReduce ban đầu là công nghệ độc quyền của Google, nó đã trở thành thuật ngữ tổng quát hóa trong thời gian gần đây.

MapReduce gồm các thủ tục: 1 Map() và 1 Reduce(). Thủ tục Map() lọc (filter) và phân loại (sort) trên dữ liệu trong khi thủ tục Reduce() thực hiện tổng hợp dữ liệu. Mô hình này dựa trên các khái niệm biến đổi của bản đồ và reduce các chức năng trong lập trình hướng chức năng. Thư viện thủ tục Map() và Reduce() được viết bằng nhiều ngôn ngữ. Cài đặt miễn phí, phổ biến nhất của MapReduce là Apache Hadoop.
### Nền tảng MapReduce hoạt động như thế nào?
#### Thủ tục Map()
Luôn có 1 master node trong hạ tầng để nhận đầu vào. Ngay sau master node là các sub-inputs / sub-problems. Các sub-problems được phân phối đến các worker nodes. Một worker node sau đó xử lý chúng. Một khi worker node hoàn thành xử lý với sub-problem, nó trả kết quả trở về master node.
#### Thủ tục Reduce()
Tất cả worker nodes trả kết quả của sub-problem đã gán cho chúng về master node. Master node thu thập kết quả và tổng hợp thành kết quả của vấn đề lớn (big problem) ban đầu đã được gán cho master node.

Nền tảng MapReduce thực hiện các thủ tục Map() và Reduce() ở trên song song và độc lập nhau. Tất cả thủ tục Map() có thể chạy song song và khi mỗi worker node hoàn thành tác vụ thì chúng gửi trở về master node. Thủ tục cụ thể này có thể rất hiệu quả khi nó được thực hiện trên một số lượng rất lớn dữ liệu (big data).
### Nền tảng MapReduce có 5 bước khác nhau:
- Chuẩn bị dữ liệu đầu vào cho Map()
- Thực thi mã Map() được cung cấp bởi người dùng
- Trộn dữ liệu xuất của Map vào Reduce Processor
- Thực thi mã Reduce() được cung cấp bởi người dùng
- Tạo dữ liệu xuất cuối cùng
### Luồng dữ liệu (dataflow) của nền tảng MapReduce:
- Input Reader
- Map Function
- Partition Function
- Compare Function
- Reduce Function
- Output Writer
MapReduce tương đương với SELECT và GROUP BY của 1 cơ sở dữ liệu quan hệ cho 1 cơ sở dữ liệu rất lớn.
### Tài liệu tham khảo
- https://www.scnsoft.com/blog/spark-vs-hadoop-mapreduce#:~:text=In%20fact%2C%20the%20key%20difference,up%20to%20100%20times%20faster.
- https://viblo.asia/p/hadoop-va-spark-big-data-framework-nao-tot-nhat-cho-ban-4dbZNqRqKYM
