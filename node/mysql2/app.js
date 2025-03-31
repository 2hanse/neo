var mysql = require('mysql2/promise');
require('dotenv').config({ path: "../../.env" });

const db = async () => {
    try {
        let connection = await mysql.createConnection({
            host: process.env.host,
            user: process.env.user,
            port: process.env.port,
            password: process.env.password,
            database: process.env.database
        });

        // select from st_info table
        let [rows] = await connection.query('SELECT * FROM st_info');
        console.log(rows);

        // make insert data
        let data = {
            st_id: "202599",
            name: "Moon",
            dept: "Computer"
        };

        // insert query
        await connection.query("INSERT INTO st_info (st_id, name, dept) VALUES (?, ?, ?)", 
            [data.st_id, data.name, data.dept]);
        console.log("\nData is inserted~!!");

        // select * query for inserted data
        [rows] = await connection.query("SELECT * FROM st_info WHERE st_id = ?", [data.st_id]);
        console.log(rows);

        // update query
        let [updateResult] = await connection.query("UPDATE st_info SET dept = ? WHERE st_id = ?", ["Game", data.st_id]);
        console.log(`\nUpdated Rows: ${updateResult.affectedRows}`);

        // select * query for updated data
        [rows] = await connection.query("SELECT * FROM st_info WHERE st_id = ?", [data.st_id]);
        console.log(rows);

        // delete query
        let [deleteResult] = await connection.query("DELETE FROM st_info WHERE st_id = ?", [data.st_id]);
        console.log(`\nDeleted Rows: ${deleteResult.affectedRows}`);

        // select * query for deleted data
        [rows] = await connection.query("SELECT * FROM st_info");
        console.log(rows);

        // 연결 종료
        await connection.end();
    } catch (error) {
        console.log(error);
    }
};

db();
