#!/usr/bin/env python2.7

import psycopg2


def main():
    # Connect to database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # Question 1
    popular_articles_query = """
    SELECT articles.title, count(*) AS views FROM log, articles
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY views DESC LIMIT 3
    """
    # Execute sql query
    c.execute(popular_articles_query)
    print("Top 3 most popular articles of all time:")
    # For each row print title of article and amount of views
    for(title, views) in c.fetchall():
        print("{} - {} views".format(title, views))
    # Add space to make different questions clear
    print("\v")

    # Question 2
    popular_authors_query = """
    SELECT authors.name, count(*) AS views
    FROM log, articles, authors
    WHERE log.path = CONCAT('/article/', articles.slug)
    AND authors.id = articles.author
    GROUP BY authors.name ORDER BY views DESC
    """
    # Execute sql query
    c.execute(popular_authors_query)
    print("Most popular authors of all time:")
    # For each row print name of author and amount of views
    for(name, views) in c.fetchall():
        print("{} - {} views".format(name, views))
    # Add space to make different questions clear
    print("\v")

    # Question 3
    request_error_query = """
    SELECT TO_CHAR(DATE(time) :: DATE, 'FMMonth dd, yyyy'),
    ROUND( 100 * (SUM(CASE WHEN status <> '200 OK'
    THEN 1 ELSE 0 END)::decimal / COUNT(status)), 2) AS error_percent
    FROM log GROUP BY DATE(time) HAVING ROUND( 100 * (SUM(CASE WHEN status
    LIKE '4%' THEN 1 ELSE 0 END)::decimal / COUNT(status)), 2) > 1
    """
    # Execute sql query
    c.execute(request_error_query)
    print("Days which more than 1% of requests lead to errors:")
    # For each row print date and error percent where it is greater than 1%
    for(date, error_percent) in c.fetchall():
        print("{} - {}% errors".format(date, error_percent))
    # Add space to make different questions clear
    print("\v")


main()
