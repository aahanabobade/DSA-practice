-- Patients With a Condition
-- Difficulty: Easy
-- Runtime: 570 ms
-- Memory: 0B
-- https://leetcode.com/problems/patients-with-a-condition/

# Write your MySQL query statement below
select patient_id   , patient_name, conditions
FROM Patients

where conditions LIKE 'DIAB1%'OR conditions LIKE '% DIAB1%';
