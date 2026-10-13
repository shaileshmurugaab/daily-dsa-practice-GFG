# LeetCode: Combine Two Tables
# Link: https://leetcode.com/problems/combine-two-tables/
# Language: Python
# Synced with CodeSync

/* Write your PL/SQL query statement below */
select firstName as FIRSTNAME,lastName as LASTNAME,city as CITY,state as STATE from Person inner join Address on Person.personId = Address.personId;
