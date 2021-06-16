-- Module 7

DROP PROCEDURE IF EXISTS ComputeOverallScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeOverallScoreForUser( IN user_id INT) BEGIN DECLARE overall_score FLOAT;

SET overall_score = (
SELECT  AVG(score)
FROM corrections AS C
WHERE C.user_id=user_id); UPDATE users 

SET overall_score = overall_score
WHERE id=user_id;
END // 
DELIMITER ; 
