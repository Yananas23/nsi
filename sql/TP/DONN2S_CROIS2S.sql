SELECT * FROM ville, evolution;
SELECT * FROM ville, evolution WHERE nom='Caullery';
SELECT nom, categorie
	FROM ville, evolution
	WHERE nom='Caullery';
	
SELECT ville.code AS code1, evolution.code AS code2, nom
	FROM ville, evolution
	WHERE nom='Caullery';
	
SELECT nom, v.code AS code1, effectif
	FROM ville AS v, evolution AS e
	WHERE nom='Caullery';
	
SELECT v.code, nom AS ville, categorie, genre, effectif
	FROM ville AS v JOIN evolution AS e ON v.code=e.code
	WHERE nom='Caullery';
	
SELECT v.code AS code, nom , categorie, genre, effectif
	FROM ville AS v JOIN evolution AS e ON v.code=e.code
	WHERE effectif=(SELECT max(effectif) FROM evolution);