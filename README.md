#Solution Link

1.
http://127.0.0.1:8000/myapp/w6

2.
http://127.0.0.1:8000/myapp/county/dinwiddie/

# Homework 7: Presenting your Data with Django

Assignment due November 16 at 1:30am.  Please accept it [here](https://classroom.github.com/assignment-invitations/b113cb352b93c0517bde542d62df9b6e).

For this assignment, you are requested to create a Django app with two views:

1. Your webpage from week 6.  Call this view `w6`.  You must use a template to separate the header/navigation from content.
2. Present a table of the republican and democratic vote share for _any_ county/city in Virginia by accessing

   http://127.0.0.1:8000/county/dinwiddie/

   Your site should deal with either upper or lower case addresses.  Hint: use string `s.lower()`.
   If you did not complete week 6, a file with the data for all years is included in this directory.

Extra credit: Review the last two pages of the [django lectures](https://github.com/harris-ippp/lectures/blob/master/07/dynamic.pdf), not yet covered, and add the ability to plot all of the counties.  N.B. that you'll probably need to do this for the final project, so you may as well do it now.
