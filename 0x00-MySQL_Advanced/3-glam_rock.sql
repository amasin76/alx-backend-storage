-- Task: List all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (2022 - MIN(year_formed)) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;
