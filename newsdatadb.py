#!/usr/bin/env python2
# "Database code" for the DB news.

# We need to import psycopg2 to allow python to interact with postgresql
import psycopg2

# We are assigning a variable to the database that we are using
DBNAME = "news"


def popular_articles():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will gather the title of each article
                then based on the title count how many times the article
                was viewed then will display the top 3 most viewed articles
                grouped by the title
            Output:
                articles
        """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT title, count(*) AS num
                        FROM articles, log
                        WHERE log.path = concat('/article/',articles.slug)
                        AND NOT PATH = '/'
                        GROUP BY title
                        ORDER BY num DESC
                        LIMIT 3;''')
    articles = c.fetchall()
    db.close()
    return articles


# We are assigning a variable the output of popular_articles
articles_list = popular_articles()


def articles_output():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will print out the question for the report
                Then will add table formatting
                Finally the table will be populated with data from our query
            Output:
                answer to question one
        """
    print " "
    print "What are the most popular three articles of all time?"
    print " "
    print " "*10 + "Title" + " "*19 + "|" + " "*2 + "Number of Views"
    print "-"*34 + "+" + "-"*18
    index = 0
    while index < 3:
        print articles_list[index][0] + " "*2 + "|" \
            + " "*2 + str(articles_list[index][1])
        index += 1
    return " "


def popular_authors():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will gather the list of authors
                then based on the view count sort by total article views
                for each author and will populate with data from our query
            Output:
                authors
        """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT name, count(*) AS page_views
                        FROM articles, authors, log
                        WHERE articles.author = authors.id
                        AND log.path = concat('/article/',articles.slug)
                        AND NOT Path = '/'
                        GROUP BY name
                        ORDER BY page_views DESC;''')
    authors = c.fetchall()
    db.close()
    return authors


# We are assigning a variable the output of popular_authors
authors_list = popular_authors()


def authors_output():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will print out the question for the report
                Then will add table formatting
                Finally the table will be populated with data from our query
            Output:
                answer to question two
        """
    print " "
    print "Who are the most popular article authors of all time?"
    print " "
    print " "*10 + "Name" + " "*10 + "|" + " "*2 + "Number of Article Views"
    print "-"*24 + "+" + "-"*26
    index = 0
    while index < len(authors_list):
        print authors_list[index][0] + " "*(24 - len(authors_list[index][0])) \
            + "|" + " "*2 + str(authors_list[index][1])
        index += 1
    return " "


def page_errors():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will gather the dates from the log table
                then based on the statuses determine the percent of errors
                for each date over 1% and populates with data from our query
            Output:
                errors
        """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT total.date,
          ROUND(((errors.page_errors*1.0) / total.page_requests), 3)
          AS failures
        FROM (
          SELECT CAST(time AS DATE) "date", count(*) AS page_errors
          FROM log
          WHERE status != '200 OK'
          GROUP BY date
        ) AS errors
        JOIN (
          SELECT CAST(time AS DATE) "date", count(*) AS page_requests
          FROM log
          GROUP BY date
          ) AS total
        ON total.date = errors.date
        WHERE (ROUND(((errors.page_errors*1.0) / total.page_requests), 3)
        > 0.01)
        ORDER BY failures DESC;''')
    errors = c.fetchall()
    db.close()
    return errors


# We are assigning a variable the output of page_errors
date_list = page_errors()


def errors_output():
    """ Function
            Input:
                There is no input for this function
            Behavior:
                The function will print out the question for the report
                Then will add table formatting
                Finally the table will be populated with data from our query
            Output:
                answer to question three
        """
    print " "
    print "On which days did more than 1% of requests lead to errors?"
    print " "
    print " "*10 + "Date" + " "*10 + "|" + " "*2 + "Percent of Errors"
    print "-"*24 + "+" + "-"*26
    index = 0
    while index < len(date_list):
        print str(date_list[index][0]) + " "*14 + "|" + " "*2 + \
            str("{:%}".format(date_list[index][1]))
        index += 1
    return " "


print articles_output()
print authors_output()
print errors_output()
