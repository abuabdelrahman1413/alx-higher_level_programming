# 0x0E. SQL - More queries

## Project Overview

This project focuses on deepening your understanding of SQL queries and database management. You'll learn about:

- Creating new MySQL users
- Managing user privileges for databases and tables
- Defining primary and foreign keys
- Using constraints like `NOT NULL` and `UNIQUE`
- Retrieving data from multiple tables in a single query
- Subqueries, JOINs, and UNION operations

## Learning Objectives

By the end of this project, you should be able to:

- Explain how to create a new MySQL user.
- Explain how to manage privileges for a user to access a database or table.
- Define what a primary key and a foreign key are.
- Explain how to use `NOT NULL` and `UNIQUE` constraints.
- Retrieve data from multiple tables using one request.
- Explain what subqueries, JOINs, and UNION operations are.

## Requirements

- **Allowed Editors**: vi, vim, emacs
- **Execution Environment**: Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
- **File Requirements**:
    - All files should end with a new line.
    - All SQL queries should have a comment just before them.
    - All files should start with a comment describing the task.
    - All SQL keywords should be in uppercase (SELECT, WHERE...).
    - A `README.md` file is mandatory at the root of the project folder.
- **Code Length**: File lengths will be tested.
- **Plagiarism**: Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Tasks

This project includes several tasks that guide you through building SQL queries for various scenarios. Each task has a specific objective and instructions. The files for each task are organized in the `0x0E-SQL_more_queries` directory.

### 0. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

### 1. Root user

Write a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server.
- The `user_0d_1` password should be set to `user_0d_1_pwd`.
- If the user `user_0d_1` already exists, your script should not fail.

### 2. Read user

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`.
- The `user_0d_2` password should be set to `user_0d_2_pwd`.
- If the database `hbtn_0d_2` already exists, your script should not fail.
- If the user `user_0d_2` already exists, your script should not fail.

### 3. Always a name

Write a script that creates the table `force_name` on your MySQL server.

- `force_name` description:
    - `id` INT
    - `name` VARCHAR(256) (can't be null)
- The database name will be passed as an argument of the `mysql` command.
- If the table `force_name` already exists, your script should not fail.

### 4. ID can't be null

Write a script that creates the table `id_not_null` on your MySQL server.

- `id_not_null` description:
    - `id` INT (with the default value 1)
    - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command.
- If the table `id_not_null` already exists, your script should not fail.

### 5. Unique ID

Write a script that creates the table `unique_id` on your MySQL server.

- `unique_id` description:
    - `id` INT (with the default value 1 and must be unique)
    - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command.
- If the table `unique_id` already exists, your script should not fail.

### 6. States table

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

- `states` description:
    - `id` INT (unique, auto-generated, can't be null, and is a primary key)
    - `name` VARCHAR(256) (can't be null)
- If the database `hbtn_0d_usa` already exists, your script should not fail.
- If the table `states` already exists, your script should not fail.

### 7. Cities table

Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

- `cities` description:
    - `id` INT (unique, auto-generated, can't be null, and is a primary key)
    - `state_id` INT (can't be null and must be a FOREIGN KEY that references the `id` of the `states` table)
    - `name` VARCHAR(256) (can't be null)
- If the database `hbtn_0d_usa` already exists, your script should not fail.
- If the table `cities` already exists, your script should not fail.

### 8. Cities of California

Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

- The `states` table contains only one record where `name = California` (but the `id` can be different).
- Results must be sorted in ascending order by `cities.id`.
- You are not allowed to use the `JOIN` keyword.
- The database name will be passed as an argument of the `mysql` command.

### 9. Cities by States

Write a script that lists all cities contained in the database `hbtn_0d_usa`.

- Each record should display: `cities.id - cities.name - states.name`.
- Results must be sorted in ascending order by `cities.id`.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 10. Genre ID by show

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

- Each record should display: `tv_shows.title - tv_show_genres.genre_id`.
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 11. Genre ID for all shows

Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

- Each record should display: `tv_shows.title - tv_show_genres.genre_id`.
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
- If a show doesn’t have a genre, display `NULL`.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 12. No genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

- Each record should display: `tv_shows.title - tv_show_genres.genre_id`.
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 13. Number of shows by genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- Each record should display: `<TV Show genre> - <Number of shows linked to this genre>`.
- The first column must be called `genre`.
- The second column must be called `number_of_shows`.
- Don’t display a genre that doesn’t have any shows linked.
- Results must be sorted in descending order by the number of shows linked.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 14. My genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres of the show Dexter.

- The `tv_shows` table contains only one record where `title = Dexter` (but the `id` can be different).
- Each record should display: `tv_genres.name`.
- Results must be sorted in ascending order by the genre name.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 15. Only Comedy

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name = Comedy` (but the `id` can be different).
- Each record should display: `tv_shows.title`.
- Results must be sorted in ascending order by the show title.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

### 16. List shows and genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows and all genres linked to that show from the database `hbtn_0d_tvshows`.

- If a show doesn’t have a genre, display `NULL` in the genre column.
- Each record should display: `tv_shows.title - tv_genres.name`.
- Results must be sorted in ascending order by the show title and genre name.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

## How to Install MySQL on Ubuntu 20.04 LTS

```bash
sudo apt update
sudo apt install mysql-server
content_copy
Use code with caution.
Markdown
How to Connect to Your MySQL Server
sudo mysql
content_copy
Use code with caution.
Bash
How to Use Container-on-Demand

Ask for a container with Ubuntu 20.04.

Connect via SSH or the Web terminal.

Start MySQL before working with it: service mysql start

How to Import a SQL Dump
# Create the database
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p

# Import the SQL dump
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
content_copy
Use code with caution.
Bash
Project Submission

When you have completed all the tasks, submit your project on your GitHub repository. Remember to follow the file naming conventions and include a README.md file describing your project.

Good luck!
content_copy
Use code with caution.
