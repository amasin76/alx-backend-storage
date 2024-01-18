-- Task: Create a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight FLOAT;
    DECLARE weighted_score FLOAT;

    SELECT SUM(weight) INTO total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE user_id = user_id;

    SELECT SUM(score * weight) INTO weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = weighted_score / total_weight
    WHERE id = user_id;
END //
DELIMITER ;
