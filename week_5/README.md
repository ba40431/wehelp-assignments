SQL 指令與各指令執行畫面的截圖
============================

**要求三**

* 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。 

        INSERT INTO `member`(`name`,`username`,`password`) VALUES ('test','test','test');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('abby','abby','abby','50');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('aaron','aaron','aaron','85');
        INSERT INTO `member`(`name`,`username`,`password`) VALUES ('kiki','kiki','kiki');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('irene','irene','irene','66');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('apple','apple','apple','37');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('emily','emily','emily','9');
        INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ('bob','bob','bob','72');
        
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-1.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

        SELECT * FROM `member`;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-2.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

        SELECT * FROM `member` ORDER BY `time` DESC;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-3.png)
        
* 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

        SELECT * FROM `member` ORDER BY `time`DESC LIMIT 1,3;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-4.png)

* 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

        SELECT * FROM `member` WHERE `username`='test';
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-5.png)
   
* 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

        SELECT * FROM `member` WHERE `username`='test' and `password`='test';
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-6.png)

* 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

        UPDATE `member` SET `name`='test2' WHERE `username`='test';
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-7.png)
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/3-7.1.png)


**要求四**

* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

        SELECT COUNT(id) FROM `member`;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/4-1.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。

        SELECT SUM(follower_count) FROM `member`;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/4-2.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

        SELECT AVG(follower_count) FROM `member`;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/4-3.png)

**要求五**

* 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

      SELECT `member_id`,`content`,`name`,`username` FROM `message` JOIN `member` ON `member_id`=`member`.`id`;
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/5-1.png)

* 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

      SELECT `member_id`,`content`,`name`,`username` FROM `message` JOIN `member` ON `member_id`=`member`.`id`
      WHERE `username`='test';
    ![](https://raw.githubusercontent.com/ba40431/wehelp-assignments/main/week_5/pic/5-2.png)



