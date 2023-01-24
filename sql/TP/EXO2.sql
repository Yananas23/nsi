SELECT v.code, nom, categorie, genre, effectif
	FROM ville AS v JOIN evolution AS e ON v.code=e.code
	WHERE v.nom='Caullery'
	ORDER BY effectif ASC;
	
SELECT nom, categorie, effectif
	FROM ville JOIN evolution ON ville.code=evolution.code
	WHERE effectif='0'
	ORDER BY categorie ASC;
	
SELECT DISTINCT nom
	FROM ville JOIN evolution on ville.code=evolution.code
	WHERE effectif>='2000' and not nom='Lille'
	ORDER BY effectif DESC;