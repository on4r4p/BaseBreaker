import sys,time,re
from baseconvert import base

tmpwordlist = ["rotter","la","le","of",'im',"et","coal","eat","saw","nos","toulouse",'zut','sony','brand','moto','chut','multi','au','bof','at','cool','c00l','pareo','ART', 'SYSTEMEDENUMERATION', 'NONCONNECTE', 'INTERNET', 'HACKERCULTURE', 'ISLENSKA', 'HIJACKING', 'GOVERNMENTRESOURCES', 'EXPORTCONTROLS', 'NSASCRYPTOKIDS', 'EXEMPLES', 'PERVASIVE', 'OZBEKCHAUZBEKCHA', 'EXPERIENCEDAFSHAR', 'FANWORKS', 'GAMES', 'KABIYE', 'ARTICLE', 'FREESOFTWAREPORTAL', 'CURRENTEVENTS', 'FILMSDERIVESDEPUIS', 'ENERGIEDUVIDE', 'TELUGU', 'GOMMEQUANTIQUE', 'ESPACEDEHILBERT', 'CESTINA', 'NEDERLANDS', 'FREEPARTICLE', 'BELARUSKAIA', 'WORLDWIDEWEB', 'WENYAN', 'THISQUANTUMWORLD', 'INTRICATION', 'ETDAUTRESENCORE', 'AUTRESMEDIAS', 'LEMOTCLEDIAEST', 'QUANTUMTHEORY', 'CATEGORIE', 'BIDOUILLABILITE', 'ORIGINALMUSICMUSIC', 'HACKTIVISME', 'BOUZEREAUP', 'NAVIGATIONMENU', 'BOSANSKI', 'ESPERANTO', 'STEPPOTENTIAL', 'NOTES', 'TROISIEMETRILOGIE', 'SURVEILLANCE', 'CHAVASHLA', 'CENSORSHIP', 'ICONINTERNETPORTAL', 'INTERNETHOMICIDE', 'AFFICHERLHISTORIQUE', 'THECLONEWARS', 'EPISODEVII', 'RDW', 'SUICIDEQUANTIQUE', 'RIBENYU', 'TECHNOTHRILLER', 'CLOUDCOMPUTING', 'COMMUNITYPORTAL', 'ZHONGWEN', 'MAGYAR', 'CYBER', 'CITERCETTEPAGE', 'STANDAGE', 'PHISHING', 'THELASTJEDI', 'ACADEMIA', 'KAZAKSHA', 'PERSONALPAN', 'ARTICLESCONNEXES', 'METASPLOITPROJECT', 'PRELOGIEA', 'YCLOPE', 'GUIDES', 'CONTACT', 'ONECRITSOUSWIKIPE', 'WOJCIECHZUREK', 'SOCIALIMPACT', 'FORCESTARWARS', 'NUMERATION', 'SPAM', 'DBLIIE', 'SYSTEMESDEMIME', 'QUBIT', 'ITALIANO', 'MATRICEDENSITE', 'ARTNET', 'TALK', 'NOTESETREFERENCES', 'ZEMAITESKA', 'ANNEXES', 'OUENCORE', 'QUANTUMMECHANICS', 'CRYPTOGRAPHY', 'ROSENHEIMP', 'CHIFFREMENT', 'UNEARMEDEGUERRE', 'MISCELLANEOUS', 'SURLADECOHERENCE', 'COMPUTERASATARGET', 'IIATTACKOFTHECLONES', 'VTE', 'IMPACTCULTUREL', 'HISTOIRE', 'IMPRIMEREXPORTER', 'SCIENTISTS', 'VARIANTES', 'BLOWFISH', 'DISCLAIMERS', 'CYBERWARFARE', 'COURSEMATERIAL', 'CREATEACCOUNT', 'SYNOPSIS', 'FENTESDEYOUNG', 'PANORAMAGENERAL', 'FTPCUHKEDUHK', 'SEEALSOCLIPPERCHIP', 'HISFORHBAR', 'CONTRAFACTUALITE', 'NOTE', 'LESMARCHES', 'PORTAILSTHEMATIQUES', 'TERMINOLOGY', 'ELLENIKA', 'DARKNET', 'SOURCE', 'ENABLEPREVIEWS', 'AGROPHYSICS', 'PIRATEOUHACKER', 'TELECHARGERCOMMEPDF', 'INTERNETMETAPHORS', 'OUTAGES', 'ATOMEDHYDROGENE', 'YUEYU', 'SYSTEMEVICESIMAL', 'THESTORYOFSTARWARS', 'ATTACKOFTHECLONES', 'ENGLISHCRIMINALLAW', 'STARWARSLUCASFILM', 'PENETRATIONTEST', 'CYBEREXTORTION', 'BIBLIOGRAPHIE', 'ANIMATEDFILM', 'SCIENCE', 'KARTULI', 'IP', 'LIRE', 'ETDELAREALITE', 'SECURITY', 'SELECTIVE', 'AIDE', 'CRYPTOSYSTEMS', 'TELEVISIONSERIES', 'CONSTANTEDEPLANCK', 'APPLICATIONLAYER', 'HISTOIRECOMMUNE', 'PRINTPUBLICATIONS', 'CHIFFREMENTPARBLOC', 'LOISDEPROBABILITES', 'ELECTRONICART', 'TAGALOG', 'TVFILMS', 'PHYSICSANDSTARWARS', 'FIJIHINDI', 'WIKIVERSITY', 'SCHRODINGEREQUATION', 'GLOBALSURVEILLANCE', 'DEUTSCH', 'IDO', 'GENERATIVEART', 'HACK', 'MAKERCULTURE', 'LESSYSTEMESADDITIFS', 'OPERATEURSUNITAIRES', 'LESSYSTEMESHYBRIDES', 'ANDDATXL', 'THEATRICALFILMS', 'RECENTCHANGES', 'INTELLIGENCE', 'ONLINEBOOKS', 'BAHASAMELAYU', 'DECALAGEDELAMB', 'ESPANOL', 'LABROUSSEETSCHALLP', 'EESTI', 'DANSDAUTRESPROJETS', 'SICILIANU', 'MODERNCRYPTOGRAPHY', 'EFFETCASIMIR', 'TEXTSFROMWIKISOURCE', 'LCENARTICLEARCHIVE', 'FAQS', 'AFFICHER', 'PARTICULELIBRE', 'INTERNETART', 'AZRBAYCANCA', 'MALTI', 'WIKIBOOKS', 'MURRAYGELLMANN', 'KAMINSKIP', 'BRANCHESOFPHYSICS', 'STRONGCRYPTOGRAPHY', 'MEDIA', 'NEARMENAN', 'TRESPASSTOCHATTELS', 'COURS', 'COMPUTERTRESPASS', 'ADVANCEDTOPICS', 'REFERENCES', 'KAMINSKIPP', 'INOTHERPROJECTS', 'POLSKI', 'USERSWORLDWIDE', 'LINKLAYER', 'MLYAALLN', 'PROTECTEDCOMPUTER', 'RUSINSKYI', 'ELECTRONICA', 'ARAGONES', 'LEGALISSUES', 'ICONPHYSICSPORTAL', 'BRYT', 'PORTHOPPING', 'SHA', 'UTILISATIONS', 'SOURCESSECONDAIRES', 'GRAVITEQUANTIQUE', 'OTHERANTHOLOGYFILMS', 'GALEGO', 'UTILISATION', 'CYBERTERRORISME', 'DESTRIPLEDES', 'COMPUTERMUSIC', 'HAROCHEETAL', 'CLONEWARS', 'KHWRDY', 'OFFICIALWEBSITE', 'APROPOSDEWIKIPEDIA', 'INTERNETS', 'SWITCHJOURNALJUN', 'APPLICATIONS', 'BAANLAA', 'WHATLINKSHERE', 'JEDIISM', 'PRINCIPEDEBASE', 'LISTEDESEXPERIENCES', 'INFRASTRUCTURE', 'LIENSEXTERNES', 'EDIT', 'INFORMATIONWARFARE', 'NOMBRESDANSLEMONDE', 'CHAINENUMERIQUE', 'CONTRIBUER', 'BASASUNDA', 'OUTILS', 'CLASSIFICATION', 'USES', 'MAINPAGE', 'WIDEWAN', 'EWOKS', 'SETTING', 'FINGERPRINTING', 'HELP', 'FUNDAMENTALS', 'VIEWHISTORY', 'INSPIRATIONS', 'KYRGYZCHA', 'NEWSFROMWIKINEWS', 'HACKERARTMENTIONS', 'SOFTWAREART', 'CLASSICAL', 'ECRITUREDESHELLCODE', 'LTPPPPMAC', 'FOUNDERS', 'MRAATTHII', 'BASHKORTSA', 'TOKYODISNEYLANDMAY', 'ONORDONNELESWEIIPK', 'FINITEPOTENTIALWELL', 'BIOPHYSICS', 'DEVELOPPEURS', 'CROWDSOURCING', 'ESPIONAGE', 'MECANIQUEQUANTIQUE', 'EPISODEVIII', 'LOGIN', 'MZIRWNY', 'SVENSKA', 'DIELIB', 'DEEPWEB', 'FONCTIONSDEHACHAGE', 'WAVEPARTICLEDUALITY', 'UCENNE', 'EPISODEIII', 'PRINTMEDIA', 'IMPORTERUNFICHIER', 'WIKINEWS', 'SOILATMOSPHERIC', 'NOMBRESENFRANCAIS', 'MAINARTICLEMALWARE', 'DONATETOWIKIPEDIA', 'CRYPTANALYSIS', 'RECHERCHER', 'JEDI', 'MATHEMATIQUES', 'WINARAY', 'VIITHEFORCEAWAKENS', 'UNIVERSETENDU', 'AFRIKAANS', 'BREZHONEG', 'AETBRYDERWINDHAMP', 'TAREC', 'GRANDEUROBSERVABLE', 'LIENPERMANENT', 'DIVISIONS', 'SPINDELELECTRON', 'INTEGRALEDECHEMIN', 'IVANEWHOPE', 'MAINARTICLEROGUEONE', 'UKRAYINSKA', 'SPECIALGENERAL', 'HISTORIQUES', 'PERFORMANCE', 'HARASSMENT', 'AITHY', 'DATATRANSFER', 'CATALA', 'MERCHANDISING', 'CLOUDIAN', 'VORO', 'REGLEDEBORN', 'FORMULATIONS', 'THEPHANTOMMENACE', 'CHIFFRES', 'GENERAL', 'HOMEHAN', 'STARWARS', 'AWARENESS', 'REBELS', 'SPHERICALBASIS', 'KNNDD', 'CONTACTPAGE', 'USERS', 'DES', 'INDUSTRY', 'COMPUTERERA', 'ANIMATEDSERIES', 'EXTERNALLINKS', 'CAMPUSCAN', 'MISTY', 'HACKING', 'GAEILGE', 'CONTRIBUTIONS', 'RUSSKII', 'TRILOGIEORIGINALE', 'DISNEYLANDDECEMBER', 'VOIRAUSSI', 'TRILOGIES', 'GOVERNANCE', 'SERPENT', 'CRYPTOWARS', 'FEATUREDCONTENT', 'CYBERDEFAMATIONLAW', 'WIKIQUOTE', 'RELATEDCHANGES', 'DRUGTRAFFICKING', 'DIAGRAMMEDENERGIE', 'READ', 'HINDII', 'FILMSDERIVES', 'EFFETTUNNEL', 'WHITECOLLARCRIME', 'FONCTIONDONDE', 'MOBILEVIEW', 'FILMSANDTELEVISION', 'ELECTRONICS', 'WIKIVERSITE', 'HARMONICOSCILLATOR', 'ANEWHOPE', 'DECHIFFREMENT', 'PRIVACYPOLICY', 'AUTHORITYCONTROL', 'MODELESTANDARD', 'ARPNDPOSPFTUNNELS', 'CYMRAEG', 'INVESTIGATION', 'LITTLEORNONE', 'SIMPLEENGLISH', 'STORAGESAN', 'QUANTUM', 'HACKERS', 'INOTHERMEDIA', 'BACKGROUND', 'CREERUNCOMPTE', 'MASQUER', 'CHATDESCHRODINGER', 'COMPUTERVIRUSES', 'BASEARITHMETIQUE', 'LISTEDENOMBRES', 'LHCT', 'LAURENTJULLIERP', 'NEPAALBHAASSAA', 'EXEMPLESDACTIONS', 'DOUBLEIDENTITE', 'PAGESSPECIALES', 'PRELOGIE', 'ASPECTSHISTORIQUES', 'ITHEPHANTOMMENACE', 'PARADOXEEPR', 'EXTENSIONS', 'DEFINITION', 'FILMS', 'VIIITHELASTJEDI', 'TOYSTOYS', 'SEARCH', 'ARTICLEAUHASARD', 'ILLEGALDROPCATCHING', 'NORSKNYNORSK', 'NOTICESDAUTORITE', 'WIKIMEDIACOMMONS', 'STARWARSPORTAL', 'HANGUGEO', 'MODIFIERLESLIENS', 'FACEBOOKPAGE', 'CREERUNLIVRE', 'ROBOTICART', 'MORETECHNICAL', 'PERMANENTLINK', 'SPECIALPAGES', 'SRPSKISRPSKI', 'DOMAINHIJACKING', 'WIRELESSWLAN', 'TELEVISION', 'FBI', 'FINDMOREABOUT', 'CHIMIEQUANTIQUE', 'SOLOASTARWARSSTORY', 'SLOVENCINA', 'ASTURIANU', 'WUYU', 'TELECOMMUTING', 'EXAMPLES', 'VM', 'TMILLL', 'EPISODEIX', 'PHYSIQUEQUANTIQUE', 'BOARISCH', 'CRYPTANALYSE', 'SYSTEMESDENOTATION', 'EPRPARADOX', 'PATOIS', 'TNSFNETBACKBONEC', 'PRINCIPE', 'CYBERGUERRE', 'AVERTISSEMENTS', 'SERVICES', 'EQUATIONDEDIRAC', 'UPLOADFILE', 'THEORIEDESQUANTA', 'POSTERITE', 'EPISODEV', 'LIMBURGS', 'PARTICLEINABOX', 'FRANCAIS', 'CRYPTOGRAPHIE', 'NORSK', 'VIEWSOURCE', 'ROGUEONE', 'JEUXVIDEO', 'ORFROMEULERSFORMULA', 'HIDDENMESSAGES', 'ACCUEIL', 'GEORGELUCAS', 'EUSKARA', 'CYBERCRIME', 'NEPAALII', 'FUTURE', 'INTRODUCTIONHISTORY', 'RANDOMARTICLE', 'SYSTEMEORDINAL', 'VIDEQUANTIQUE', 'HOLIDAYSPECIAL', 'BAHASAINDONESIA', 'QUANTUMENTANGLEMENT', 'CRYPTOLOGIE', 'RINZLERPP', 'CULTURALIMPACT', 'ELEMENTWIKIDATA', 'PREQUELTRILOGY', 'DEMOSCENE', 'PRINTEXPORT', 'IX', 'ELECTRONICARTMUSIC', 'NUMERATIONARCHIVE', 'AUTRESSYSTEMES', 'BERNARDDESPAGNAT', 'ETHICSANDPRINCIPLES', 'HISTOIRES', 'NOTATIONBRAKET', 'SINHL', 'CYBERHEIST', 'CODE', 'PROGRAMMING', 'MENUDENAVIGATION', 'GLOBEICON', 'PAGESLIEES', 'SHQIP', 'CONTEMPORAINES', 'DISNEYLANDPARISMAY', 'FREENET', 'TWOFISH', 'MINGDENGNGU', 'HISTORIQUE', 'PHYSICSWITH', 'OTHERPLANNEDFILMS', 'CHIFFREARABOINDIEN', 'SPIN', 'TECHNIQUECOURANTE', 'ENERGYMOTION', 'EPISODEVI', 'AES', 'ABOUTWIKIPEDIA', 'DOWNLOADASPDF', 'BRANCHES', 'MONGOL', 'HACKERARTISTS', 'CYBERTERRORISM', 'HOSTILITYTOSECRECY', 'POWEREDBYMEDIAWIKI', 'ETATQUANTIQUE', 'REVENGEOFTHESITH', 'PROTOCOLS', 'DESLORSILVIENT', 'YYIDYSH', 'TECHNOLOGY', 'ACTIVITEDESCROC', 'HAYEREN', 'ALEMANNISCH', 'EXPERIENCEDASPECT', 'ROMANS', 'AETBLAURENTJULLIERP', 'CLEETSECURITE', 'ORDINATEURQUANTIQUE', 'MOTCLECRYPTO', 'ELECTRONICBUSINESS', 'RE', 'DSASIGNATURE', 'NOVELSLISTOFNOVELS', 'THEFORCEAWAKENS', 'ANTHOLOGYFILMS', 'LATINA', 'PHASEGEOMETRIQUE', 'VIRETURNOFTHEJEDI', 'EPISODEI', 'SLOVENSCINA', 'TURKCE', 'INTERPRETATIONS', 'SEEALSO', 'SYSTEMEUNAIRE', 'CHIFFREDECESAR', 'TROISIEMETRILOGIEA', 'LEGISLATION', 'RYDERWINDHAMP', 'CHANGINGSITUATION', 'TMRCHACKERS', 'POTENTIELQUANTIQUE', 'AUDIO', 'DISCUSSION', 'MALWARE', 'INTERNETLAYER', 'LUMBAART', 'AND', 'ACCESS', 'SUOMI', 'MODIFIERLECODE', 'STARWARSDAY', 'BURIAAD', 'DEVELOPERS', 'BURNINGMANFESTIVAL', 'LIVEATTRACTIONS', 'DIAGRAMMEDEFEYNMAN', 'TECHNOLOGIEETARMES', 'PARADOXES', 'SAVEBROWSINGGOOGLE', 'METROPOLITANMAN', 'GIANCARLOGHIRARDI', 'SCOTS', 'TOOLS', 'ORIGINALTRILOGY', 'ACTIVITESALARIEE', 'BANDESDESSINEES', 'GEORGELUCASEN', 'DANSK', 'DIVERS', 'JONATHANWRINZLERP', 'DANSDAUTRESLANGUES', 'THEORIECSM', 'LIENEXTERNE', 'SUBSTANTIAL', 'LIETUVIU', 'COMICS', 'SUIVIDESPAGESLIEES', 'ECOLEDECOPENHAGUE', 'FERMER', 'BANLAMGU', 'EQUATIONS', 'TECHNIQUESMODERNES', 'ROMANA', 'USAGE', 'NOVELS', 'ASPECTSJURIDIQUES', 'QUANTUMCOMPUTING', 'CRITIQUES', 'CATEGORIES', 'EDITLINKS', 'ESPECES', 'NSAINVOLVEMENT', 'COMICSLISTOFCOMICS', 'STEGANOGRAPHIE', 'INTERACTION', 'EXISTENCEDESQUANTA', 'CLASSICCRYPTOGRAPHY', 'WIKIMEDIAFOUNDATION', 'AGENCIES', 'EXPERIMENTS', 'VIDEOGAMES', 'CINEMA', 'CROWDFUNDING', 'FAIREUNDON', 'COMPUTERASATOOL', 'SHOW', 'CREATEABOOK', 'EPISODEIV', 'BYSPECIALITY', 'COMMUTATEUR', 'RINZLERP', 'PNJAABII', 'ATTRACTIONS', 'RETURNOFTHEJEDI', 'SEQUELTRILOGY', 'BIBLIOGRAPHY', 'OCCITAN', 'PHISHINGSCAMS', 'CHIFFREDEVIGENERE', 'COMMUNAUTE', 'STEPHENHAWKING', 'SOURCESPRIMAIRES', 'CASGENERAL', 'SLUNSKI', 'NUMERATIONROMAINE', 'PROHIBITIONS', 'OTHERSCIENCES', 'DISNEYLANDJUNE', 'COOKIESTATEMENT', 'DISNEYLANDPARISJULY', 'LRBY', 'ONWIKIBOOKS', 'BOOKINTERNET', 'PIEMONTEIS', 'PHILANTHROPY', 'INTERPRETATION', 'LATVIESU', 'MULTIMEDIAPROJECTS', 'MODIFIER', 'BACKBONE', 'THEORIEQUANTIQUE', 'TELECOMMUNICATIONS', 'UNIXPHILOSOPHY', 'CONCEPTS', 'DOCUMENTEDCASES', 'NANOSCALE', 'DEBUTERSURWIKIPEDIA', 'WIKIVOYAGE', 'AESTIMATE', 'TRANSPORTLAYER', 'IIIREVENGEOFTHESITH', 'PAGEINFORMATION', 'TOCHIKI', 'COLONNESDTEISA', 'BANNERLOGO', 'PAGESEMIPROTECTED', 'TATARCHATATARCA', 'ETHIQUE', 'CHIFFREAFFINE', 'SOMMAIRE', 'TRILOGIEORIGINALEA', 'ASMIIYAA', 'WAVESFIELDS', 'AUDIODRAMAS', 'MEDIACULTURE', 'BYSPATIALSCOPE', 'CONTACTWIKIPEDIA', 'UNIVERS', 'HRVATSKI', 'DIGITALART', 'CITETHISPAGE', 'HISTORY', 'PNJBY', 'FERMIONSETBOSONS', 'GNDNDL', 'ENERGYUSE', 'LETTREDUMOTCLE', 'PORTUGUES', 'FURTHERREADING', 'CONTENTS', 'ALBERTORIMINI', 'SECONNECTER', 'ENGLISH', 'OUVRAGESDINITIATION', 'THEMES', 'MSR', 'COMPUTERART', 'MUSICOFSTARWARS', 'NEARFIELDNFC', 'PHILOSOPHY', 'INTERLINGUA', 'PENALTIES', 'MODERNPHYSICS', 'SEMANTICWEB', 'PRINTABLEVERSION', 'TIENGVIET', 'BODYBAN', 'UNEENC', 'YEOCPL', 'DROIDS', 'STARWARSLOGOSVG', 'LANGUAGES', 'MNMAABHAASAA', 'VERSIONMOBILE', 'ICON', 'NOTLOGGEDIN', 'SEEALSOQUANTUMLOGIC', 'WIKIPEDIASTORE', 'SOLO', 'INTERNETSUICIDEPACT', 'PLANETES', 'WIKIDATAITEM', 'SITH', 'ESTREMENU', 'COMMUNICATION', 'VERSIONIMPRIMABLE', 'BLGARSKI', 'VOIRLETEXTESOURCE', 'ABETCRYDERWINDHAMP', 'EPISODEII', 'FRSY', 'MAKEDONSKI', 'HACKINGMODERNE', 'LOCALLAN', 'THEINTERNETSOCIETY','9gag','quality','qualite','you','got','merde','egale','egalite','equal','equality','message','sage','basique','basic','numeric','numero','numerique','nombre','table','please','fasses','tuclick','clique','click','ok','vaut','va','vas','en','mort','decede','affine','mathematique','nobel','prix','fonction','homme','grand','toitu','ils','vous','nous','tu','je','lol','tribulation','moimeme','renseigne','crucifix','hacking','hacker','gameboycolor','apprendre','program','progr','cettefois','biencettefois','boncettefois','popcorn','ducoups','important','salut','newyork','graal','saintgraal','jeanpierre','equipier','equip','equipement','obtenir','pourquoi','alors','accident','rupee','animationmagic','zeldagame','capcom','sortisur','sortien','quatrevingt','milleneufcentving','neufcent','milleneuf','quatre','cinq','sept','neuf','sursnes','delasnes','lasnes','snes','amateur','kidnap','kidnaping','meticuleux','ridiculous','ridicule','aubout','altgr','proverbe','silvousplait','please','charger','willbe','nonmerci','observation','observe',"seuil",'solaire','luciole','realisa','sacrifi','sacrifice','attendez','dunbaton','msdos','youlearn','appliquer','seeyoulater','templier','granted','access','bingo',"formidable","ascii",'fleuron','jeveux','jepeux','collector','compromi','commepromi','newgamecrack','cracking','gamecrack','laforme','rejoins','justement','juste','area','whydoes','whyare','whydo','proteger','ellesappelle','ilya','indique','ahok','faites','jefais','jesais','desole','drole','brillament','brillant','lecoffre','pourouvrir','coffre','tresor','reflechir','nombre','ilfaudrait','excluant','technique','hercule','game','exceptionnelle','exceptionelle','exception','exemple','dernier','final','message','prive','homme','devant','aimable', 'aime', 'relever', 'des', 'defis', 'ambitieux', 'amical', 'applique', 'articule', 'artiste', 'assure', 'attentionne', 'autonome', 'bonne', 'resistance', 'au', 'stress', 'calme', 'competent', 'comprehensif', 'consciencieux', 'consequent', 'creatif', 'curieux', 'delicat', 'determine', 'devoue', 'digne', 'de', 'confiance', 'diplomate', 'doue', 'efficace', 'enthousiaste', 'esprit', 'analyse', 'esprit', "equipe", 'esprit', 'de', 'competition', 'esprit', 'scientifique', 'fiable', 'honnete', 'imaginatif', 'ingenieux', 'innovateur', 'inventif', 'logique', 'loyal', 'meticuleux', 'minutieux', 'novateur', 'optimiste', 'organise', 'original', 'ouvert', 'patient', 'perseverant', 'perspicace', 'persuasif', 'poli', 'ponctuel', 'positif', 'pratique', 'precis', 'prevenant', 'prevoyant', 'prudent', 'reflechi', 'responsable', "adapte", 'facilement', 'sens', 'de', "lhumour", 'serieux', 'sincere', 'sociable', 'souple', 'spontane', 'stable', 'sympathique', 'tenace','perseverance','courage','patience','attaque','ordinateur','mais','encore','bientot','vigenere','mathgl','merci','animation','animateur','preuve','hoho','hihi','hehe','devez','termine','voila','fini','phrase','dechiffre','encoder','triforce','zelda','chiffrage','contest','newbie','difficile','super','cool','chiffrement','crypto','cryptographie','code','niveau','cette','sexy','jesperequ','epreuve','challenge','valider','super','felicitation','motdepasse','trouve','avez','vous','bravo','password','autre', 'apres', 'regarder', 'toujours', 'puis', 'jamais', 'cela', 'aimer', 'non', 'heure', 'croire', 'cent', 'monde', 'donc', 'enfant', 'fois', 'seul', 'autre', 'entre', 'vers', 'chez', 'demander', 'jeune', 'jusque', 'tres', 'moment', 'rester', 'repondre', 'tout', 'tete', 'pere', 'fille', 'mille', 'premier', 'car', 'entendre', 'ni', 'bon', 'trois', 'coeur', 'ainsi', 'an', 'quatre', 'un', 'terre', 'contre', 'dieu', 'monsieur', 'voix', 'penser', 'quel', 'arriver', 'maison', 'devant', 'coup', 'beau', 'connaitre', 'devenir', 'air', 'mot', 'nuit', 'sentir', 'eau', 'vieux', 'sembler', 'moins', 'tenir', 'ici', 'comprendre', 'oui', 'rendre', 'toi', 'vingt', 'depuis', 'attendre', 'sortir', 'ami', 'trop', 'porte', 'lequel', 'chaque', 'amour', 'pendant', 'deja', 'pied', 'tant', 'gens', 'parce que', 'nom', 'vivre', 'reprendre', 'entrer', 'porter', 'pays', 'ciel', 'avant', 'frere', 'regard', 'chercher', 'ame', 'cote', 'mort', 'revenir', 'noir', 'maintenant', 'nouveau', 'ville', 'rue', 'enfin', 'appeler', 'soir', 'chambre', 'mourir', 'pas', 'partir', 'cinq', 'esprit', 'soleil', 'dernier', 'jeter', 'dix', 'roi', 'etat', 'corps', 'beaucoup', 'suivre', 'bras', 'ecrire', 'blanc', 'montrer', 'tomber', 'place', 'ouvrir', 'ah', 'parti', 'assez', 'leur', 'cher', 'voila', 'annee', 'loin', 'point', 'visage', 'bruit', 'lettre', 'franc', 'fond', 'force', 'arreter', 'perdre', 'commencer', 'paraitre', 'aucun', 'marcher', 'milieu', 'saint', 'idee', 'presque', 'ailleurs', 'travail', 'lumiere', 'long', 'seulement', 'mois', 'fils', 'neuf', 'tel', 'lever', 'raison', 'effet', 'gouvernement', 'permettre', 'pauvre', 'asseoir', 'point', 'plein', 'personne', 'vrai', 'peuple', 'fait', 'parole', 'guerre', 'toute', 'ecouter', 'pensee', 'affaire', 'quoi', 'matin', 'pierre', 'monter', 'bas', 'vent', 'doute', 'front', 'ombre', 'part', 'maitre', 'aujourdhui', 'besoin', 'question', 'apercevoir', 'recevoir', 'mieux', 'peine', 'tour', 'servir', 'oh', 'autour', 'pres', 'finir', 'famille', 'pourquoi', 'souvent', 'rire', 'dessus', 'madame', 'sorte', 'figure', 'droit', 'peur', 'bout', 'lieu', 'silence', 'gros', 'chef', 'eh', 'six', 'bois', 'mari', 'histoire', 'crier', 'jouer', 'feu', 'tourner', 'doux', 'longtemps', 'fort', 'heureux', 'comme', 'garder', 'partie', 'face', 'mouvement', 'fin', 'reconnaitre', 'quitter', 'personne', 'comment', 'route', 'des', 'manger', 'livre', 'arbre', 'courir', 'cas', 'huit', 'lorsque', 'mur', 'ordre', 'continuer', 'bonheur', 'oublier', 'descendre', 'haut', 'interet', 'cacher', 'lun', 'chacun', 'profond', 'argent', 'cause', 'poser', 'autant', 'est', 'travers', 'grand', 'instant', 'facon', 'dabord', 'oeil', 'tirer', 'forme', 'presenter', 'ajouter', 'agir', 'retrouver', 'chemin', 'cheveu', 'offrir', 'surtout', 'certain', 'plaisir', 'suite', 'apprendre', 'malgre', 'tuer', 'rouge', 'sang', 'retourner', 'rencontrer', 'sentiment', 'fleur', 'cependant', 'service', 'plusieurs', 'table', 'vite', 'paix', 'envoyer', 'moyen', 'dormir', 'pousser', 'lit', 'humain', 'voiture', 'rappeler', 'etre', 'lire', 'general', 'nature', 'or', 'pouvoir', 'nouveau', 'francais', 'joie', 'sept', 'tard', 'president', 'pourtant', 'bouche', 'changer', 'petit', 'froid', 'compter', 'occuper', 'sens', 'cri', 'cheval', 'loi', 'sombre', 'ci', 'sur', 'espece', 'voici', 'ancien', 'tandis que', 'frapper', 'ministre', 'puisque', 'selon', 'travailler', 'expliquer', 'propre', 'obtenir', 'rentrer', 'mal', 'pleurer', 'essayer', 'repeter', 'societe', 'parfois', 'politique', 'oreille', 'payer', 'politique', 'apporter', 'fenetre', 'derriere', 'possible', 'fortune', 'compte', 'champ', 'manier', 'vraiment', 'immense', 'action', 'boire', 'public', 'garcon', 'pareil', 'bleu', 'sourire', 'couleur', 'coucher', 'papier', 'dautres', 'mal', 'fort', 'bientot', 'causer', 'piece', 'montagne', 'sol', 'oeuvre', 'partout', 'trente', 'exister', 'cours', 'raconter', 'serrer', 'songer', 'desir', 'manquer', 'cour', 'nommer', 'bord', 'douleur', 'conduire', 'salle', 'saisir', 'premier', 'comment', 'projet', 'demeurer', 'simple', 'etude', 'remettre', 'journal', 'geste', 'disparaitre', 'battre', 'toucher', 'situation', 'oiseau', 'necessaire', 'exemple', 'siecle', 'apparaitre', 'souffrir', 'million', 'prix', 'groupe', 'centre', 'malheur', 'honneur', 'fermer', 'accepter', 'garde', 'mauvais', 'tendre', 'naitre', 'sauver', 'entier', 'parmi', 'probleme', 'larme', 'avancer', 'chien', 'peau', 'reste', 'traverser', 'nombre', 'debout', 'mesure', 'social', 'souvenir', 'article', 'vue', 'couvrir', 'age', 'gagner', 'systeme', 'long', 'former', 'plaire', 'embrasser', 'reve', 'oser', 'afin de', 'passion', 'auquel', 'rapport', 'refuser', 'important', 'decider', 'produire', 'soldat', 'levre', 'signe', 'verite', 'charger', 'mariage', 'meler', 'certain', 'plan', 'cesser', 'ressembler', 'dos', 'marche', 'souvenir', 'dame', 'chanter', 'plutot', 'conseil', 'sou', 'triste', 'coin', 'jardin', 'joli', 'soit', 'empecher', 'doigt', 'objet', 'fer', 'lendemain', 'lentement', 'combien', 'approcher', 'prier', 'train', 'esperer', 'papa', 'different', 'valeur', 'jeu', 'echapper', 'glisser', 'secret', 'haut', 'vieillard', 'briller', 'docteur', 'bruler', 'terrible', 'placer', 'ton', 'jambe', 'juger', 'suffire', 'endroit', 'minute', 'atteindre', 'nuage', 'presence', 'fou', 'epaule', 'leger', 'feuille', 'liberte', 'journee', 'libre', 'annoncer', 'avenir', 'sourire', 'hier', 'resultat', 'elever', 'acheter', 'mener', 'preparer', 'pourquoi', 'hotel', 'semaine', 'foret', 'assurer', 'pur', 'qualite', 'prince', 'bien', 'egalement', 'deviner', 'medecin', 'considerer', 'volonte', 'seigneur', 'effort', 'quelque', 'vert', 'art', 'moindre', 'demain', 'quarante', 'cinquante', 'foule', 'appartenir', 'aussitot', 'ligne', 'representer', 'tromper', 'interieur', 'vendre', 'beaute', 'riche', 'craindre', 'etrange', 'emporter', 'ensuite', 'soin', 'naturel', 'hasard', 'puis', 'condition', 'quinze', 'classe', 'voyage', 'aupres', 'present', 'caractere', 'attention', 'gris', 'or', 'rouler', 'faible', 'posseder', 'scene', 'difficile', 'francais', 'reveiller', 'foi', 'aider', 'decouvrir', 'odeur', 'choisir', 'musique', 'oncle', 'evenement', 'prononcer', 'village', 'taire', 'envie', 'midi', 'ensemble', 'expression', 'herbe', 'vieux', 'pluie', 'pres', 'bas', 'rever', 'appuyer', 'etendre', 'apres', 'general', 'lutte', 'trembler', 'reponse', 'grace', 'espace', 'habitude', 'defendre', 'memoire', 'creer', 'grave', 'maintenir', 'verre', 'campagne', 'quelquun', 'juge', 'genou', 'impossible', 'fete', 'indiquer', 'pret', 'promettre', 'relever', 'abandonner', 'ignorer', 'large', 'parent', 'colere', 'exprimer', 'etoile', 'devoir', 'conscience', 'existence', 'accompagner', 'immobile', 'adresser', 'observer', 'juste', 'puissance', 'matiere', 'sable', 'separer', 'marier', 'prevoir', 'vivant', 'accord', 'hiver', 'retour', 'autrefois', 'genre', 'dautres', 'vif', 'amener', 'obliger', 'acte', 'image', 'horizon', 'eclairer', 'poursuivre', 'danger', 'livrer', 'role', 'escalier', 'gout', 'bete', 'ceci', 'recherche', 'membre', 'pain', 'phrase', 'contenir', 'rire', 'fuir', 'couler', 'terme', 'eaux', 'moyen', 'police', 'rocher', 'proposer', 'tranquille', 'unique', 'eprouver', 'retenir', 'type', 'vin', 'superieur', 'attacher', 'voler', 'sec', 'justice', 'epoque', 'passage', 'somme', 'science', 'surprendre', 'cote', 'doucement', 'gauche', 'faute', 'ecole', 'bon', 'ensemble', 'rayon', 'briser', 'sujet', 'imaginer', 'diriger', 'douze', 'en', 'lune', 'dernier', 'avis', 'parvenir', 'ouvert', 'penetrer', 'poete', 'meilleur', 'paysan', 'remarquer', 'chair', 'eviter', 'soudain', 'succes', 'ile', 'etablir', 'reussir', 'pencher', 'habiter', 'entourer', 'declarer', 'detail', 'arme', 'realite', 'confiance', 'masse', 'crise', 'etonner', 'poste', 'dresser', 'durer', 'depuis', 'FAUX', 'fixer', 'enorme', 'principe', 'direction', 'taille', 'desirer', 'sante', 'ventre', 'marche', 'puissant', 'simplement', 'environ', 'tellement', 'arracher', 'entrainer', 'soutenir', 'couper', 'trou', 'inconnu', 'pont', 'lune', 'dehors', 'certes', 'beaux', 'robe', 'douter', 'retirer', 'cesse', 'brusquement', 'entree', 'source', 'camarade', 'dent', 'quant a', 'connaissance', 'cou', 'but', 'promener', 'vague', 'element', 'fil', 'voie', 'nez', 'forcer', 'particulier', 'discours', 'maladie', 'chaleur', 'gloire', 'vide', 'examiner', 'revoir', 'aide', 'debut', 'ennemi', 'second', 'aile', 'flamme', 'chaise', 'lourd', 'sein', 'veritable', 'toit', 'remplir', 'terminer', 'vaste', 'nu', 'poussiere', 'nord', 'tenter', 'emotion', 'hors', 'un', 'remonter', 'revolution', 'theatre', 'armee', 'court', 'noir', 'appartement', 'semblable', 'installer', 'haine', 'jeune', 'position', 'seconde', 'frais', 'appel', 'soulever', 'espoir', 'allumer', 'imposer', 'avant', 'respirer', 'arriere', 'baisser', 'droite', 'poitrine', 'mort', 'jeunesse', 'bureau', 'sac', 'etranger', 'courage', 'souffler', 'jaune', 'page', 'etranger', 'etc', 'miser', 'passe', 'rapide', 'digne', 'chaud', 'propos', 'attirer', 'preter', 'clair', 'amuser', 'occasion', 'voile', 'eclater', 'importance', 'quartier', 'soi', 'auteur', 'religion', 'palais', 'reunir', 'traiter', 'flot', 'intelligence', 'tantot', 'voisin', 'carte', 'secret', 'animal', 'ete', 'trainer', 'cabinet', 'morceau', 'employer', 'capable', 'souffrance', 'marquer', 'prouver', 'importer', 'titre', 'desert', 'facile', 'spectacle', 'exiger', 'reposer', 'depart', 'fier', 'danser', 'demande', 'saluer', 'lueur', 'joue', 'saint', 'accorder', 'priere', 'achever', 'avouer', 'distinguer', 'emmener', 'fonction', 'durant', 'haut', 'aspect', 'sommeil', 'eclat', 'moitie', 'demi', 'calme', 'contraire', 'colline', 'agiter', 'hesiter', 'terrain', 'rare', 'poids', 'sonner', 'changement', 'charge', 'davantage', 'composer', 'enlever', 'poche', 'rejoindre', 'son', 'interieur', 'veille', 'ramener', 'fruit', 'complet', 'etudier', 'partager', 'croix', 'suivant', 'chasser', 'interrompre', 'eloigner', 'tresor', 'compagnie', 'etroit', 'cuisine', 'reduire', 'engager', 'egal', 'empire', 'nation', 'eteindre', 'recommencer', 'sauter', 'plaindre', 'conversation', 'soiree', 'violent', 'impression', 'trait', 'devant', 'preferer', 'reveler', 'sien', 'magnifique', 'desespoir', 'temoin', 'visite', 'respect', 'solitude', 'subir', 'dela', 'prochain', 'anglais', 'rapporter', 'couter', 'reflechir', 'officier', 'remercier', 'deposer', 'fauteuil', 'fumer', 'tot', 'affirmer', 'relation', 'fumee', 'convenir', 'branche', 'malade', 'circonstance', 'ouvrage', 'compagnon', 'vetir', 'experience', 'port', 'accomplir', 'avec', 'resoudre', 'plonger', 'goutte', 'mien', 'chant', 'detruire', 'combat', 'personnage', 'aventure', 'interesser', 'disposer', 'absence', 'machine', 'aucun', 'grace', 'chaine','louable','cepasse','lepasse','cepass','lepass','lecode','indice','melanger','biologie','fichier','telecharge','telecharger','rapide','cecode','jetoffre','paspasser','jevoudrai','jeveux','cruel','lumiere','examen','examine','lemdp','exclu','exclusif','decode','vicieux','pouvoir','sword','epee','donjon','relique','deesse','legend','courage','sagesse','force','devant','variante','qualite','homosexu','coeurloyal','manque','unbon','puissant','passant','trouve','lemot','moment','finalement','aufinal','facilement','passage','zodiac','coeur','resoudre','resolu','reussi','casser','bruteforce','complique','vertue','virtual','virtuel','possible','impossible','suppose','moral','moralite','facile','difficile','merci','vous','ceque','hyrule','passer','chemin','merite','entoutcas','limite','depasser','imagine','imagination','dessin','converti','decimal','jeuvideo','link','epona','ganondo','confirme','valid','passeur','attaque','problematique','probleme','probable','parcequ','google','okjecpas','okjecpassi','okjecpasce','methode','principe','principale','personnage','personne','video','animation','passe','dessinateur','passeest','dernier', 'final', 'message', 'prive', 'homme', 'devant', 'aimable', 'aime', 'relever', 'des', 'defis', 'ambitieux', 'amical', 'applique', 'articule', 'artiste', 'assure', 'attentionne', 'autonome', 'bonne', 'resistance', 'au', 'stress', 'calme', 'competent', 'comprehensif', 'consciencieux', 'consequent', 'creatif', 'curieux', 'delicat', 'determine', 'devoue','victoire','decision','decider','decide','decidement','dignede','etesdigne','esdigne','dignite', 'confiance', 'diplomate', 'doue', 'efficace', 'enthousiaste', 'esprit', 'analyse', 'esprit', 'equipe', 'esprit', 'de', 'competition', 'esprit', 'scientifique', 'fiable', 'honnete', 'imaginatif', 'ingenieux', 'innovateur', 'inventif', 'logique', 'loyal', 'meticuleux', 'minutieux', 'novateur', 'optimiste', 'organise', 'original', 'ouvert', 'patient', 'perseverant', 'perspicace', 'persuasif', 'poli', 'ponctuel', 'positif', 'pratique', 'precis', 'prevenant', 'prevoyant', 'prudent', 'reflechi', 'responsable', 'adapte', 'facilement', 'sens', 'de', 'lhumour', 'serieux', 'sincere', 'sociable', 'souple', 'spontane', 'stable', 'sympathique', 'tenace', 'perseverance', 'courage', 'patience', 'attaque', 'ordinateur', 'mais', 'encore', 'bientot', 'vigenere', 'mathgl', 'merci', 'animation', 'animateur', 'preuve', 'hoho', 'hihi', 'hehe', 'devez', 'termine', 'voila', 'fini', 'phrase', 'dechiffre', 'encoder', 'triforce', 'zelda', 'chiffrage', 'contest', 'newbie', 'difficile', 'superman', 'cool', 'chiffrement', 'crypto', 'cryptographie', 'code', 'niveau', 'cette', 'sexy', 'jesperequ', 'epreuve', 'challenge', 'valider','password','pour','bravo','www','okmerci','okmec','delta','quela','quele','chercher','newbie','arme','limonade','citron','marmelade','acide','macintosh','proteine','cestca','cestcela','comme','commecela','decodeur','abimer','codon','exode','grosses', 'version', 'compagnie', 'richard', 'internet', 'machine', 'produce', 'follows', 'grande', 'faciles', 'other', 'homme', 'actionrpg', 'watchtrois', 'statut', 'topped', 'acting', 'swords', 'decouvrant', 'endroits', 'team', 'trilogy', 'alongside', 'flash', 'frequemment', 'famitsu', 'fond', 'would', 'impraticables', 'container', 'records', 'datant', 'time', 'casey', 'actionadventure', 'nabooru', 'spirituelle', 'fitzgerald', 'lune', 'speak', 'restless', 'compositeurla', 'devenue', 'scott', 'japan', 'prequel', 'dura', 'space', 'anyone', 'bound', 'knowing', 'vingtquatre', 'looks', 'scellele', 'satellite', 'satellaview', 'male', 'gibdos', 'lambiance', 'reprend', 'engendrant', 'akito', 'kids', 'gaining', 'someone', 'molina', 'indispensable', 'mind', 'traditionnelle', 'owsen', 'sintitule', 'enter', 'platformer', 'thus', 'overhead', 'zeldaa', 'rapport', 'supposent', 'evolution', 'nourrissent', 'king', 'until', 'adventuresthe', 'effrois', 'ishikawa', 'adventure', 'serait', 'peignent', 'minutes', 'gamers', 'rupeeland', 'skimo', 'ruto', 'featuring', 'asks', 'wildsthe', 'elevees', 'croissant', 'serie', 'gamespys', 'aout', 'donjon', 'usual', 'compass', 'wrote', 'sailing', 'display', 'style', 'seamless', 'possesses', 'computer', 'intended', 'completed', 'face', 'directly', 'reduire', 'hourglassbilly', 'presentation', 'appeared', 'nombreux', 'classified', 'lenticular', 'names', 'sticker', 'majeure', 'spell', 'danse', 'interactions', 'incarne', 'iwata', 'passant', 'point', 'love', 'reliant', 'apparition', 'sometimes', 'breath', 'fitzgeralds', 'developing', 'satellitebased', 'listup', 'presentes', 'accession', 'releasing', 'prenait', 'mounted', 'stores', 'james', 'grace', 'sachant', 'shook', 'notably', 'euxmemes', 'manga', 'graeme', 'freedom', 'sworduniversimage', 'visqueuse', 'trouve', 'spinoffs', 'affirme', 'retrospective', 'connexion', 'development', 'lobjet', 'underground', 'celebrated', 'apprend', 'around', 'hack', 'royale', 'oiseaux', 'travailler', 'grown', 'lapparition', 'gallery', 'denfance', 'nouveautes', 'assassins', 'compilation', 'supplementaire', 'nomme', 'manner', 'songs', 'cooperative', 'pathways', 'minako', 'ciblee', 'simple', 'plotlinesthe', 'principally', 'branch', 'trop', 'alter', 'tecmo', 'gamestop', 'arme', 'japonen', 'lacs', 'becomes', 'giving', 'rockstars', 'pirates', 'annees', 'climats', 'celebrate', 'puzzle', 'possible', 'flashbackquete', 'translator', 'observation', 'dream', 'nouvelle', 'international', 'mondes', 'rerelease', 'sound', 'avec', 'montagnard', 'desire', 'epic', 'about', 'enfants', 'short', 'mettre', 'douvrir', 'gametrailers', 'number', 'seeing', 'fonctionnalites', 'showcased', 'global', 'editee', 'lost', 'childhood', 'empirehouser', 'compressed', 'deroule', 'liberte', 'plusieurs', 'racetrack', 'declin', 'gamer', 'awards', 'promenades', 'involved', 'dautres', 'sauvegarde', 'lock', 'beyond', 'evenements', 'facultative', 'early', 'fois', 'bestiale', 'lemplacement', 'delayed', 'vigil', 'making', 'doreesles', 'coworkers', 'australiathe', 'suit', 'nintendoannees', 'cooperation', 'installments', 'revient', 'began', 'consisted', 'facteurs', 'interviews', 'dires', 'celebre', 'collectively', 'york', 'hunt', 'dutiliser', 'compromise', 'levelbased', 'capacite', 'scoresas', 'orne', 'representatifs', 'care', 'encapuchonnees', 'members', 'extremement', 'lorigine', 'filet', 'imprisoning', 'horseback', 'medieval', 'wagners', 'dessin', 'seul', 'vraiment', 'items', 'pitch', 'parallelevictoire', 'arguably', 'reste', 'snes', 'similar', 'histoire', 'devoilant', 'body', 'communaute', 'venue', 'melangeant', 'voeu', 'colossus', 'flots', 'sheik', 'miniiles', 'echanges', 'prend', 'miyamoto', 'collectorsune', 'shrunk', 'acorn', 'mitigees', 'skulltulas', 'direct', 'licence', 'plus', 'sharpened', 'enfant', 'lemarchand', 'daemon', 'critiquee', 'durant', 'shout', 'highly', 'players', 'gladiators', 'vogel', 'writer', 'vowed', 'skyward', 'dessous', 'redmond', 'forests', 'evolue', 'ganonthe', 'sheikahs', 'ambiance', 'among', 'conference', 'achieve', 'resolution', 'musique', 'francis', 'goldcoloured', 'layout', 'gallinace', 'telecommande', 'serieun', 'scholastic', 'novels', 'data', 'lequel', 'accorde', 'adulteganon', 'tente', 'overworld', 'intermission', 'could', 'terrifiante', 'righteous', 'returned', 'miyazaki', 'definie', 'autres', 'exclusivement', 'rereleased', 'into', 'espace', 'reach', 'midjune', 'styles', 'quinze', 'france', 'creaturesthe', 'develop', 'philips', 'systems', 'tournee', 'desert', 'official', 'comportant', 'sortie', 'zeldail', 'descends', 'developers', 'dorefah', 'barton', 'loccasionle', 'legends', 'parcourant', 'devenements', 'atari', 'presence', 'officiel', 'highdefinition', 'insectes', 'skimos', 'omen', 'colin', 'preordered', 'brosin', 'apprehensively', 'epoch', 'source', 'caves', 'real', 'approaches', 'ethereal', 'taille', 'pure', 'puissent', 'mirabella', 'gannon', 'detail', 'personnage', 'dapparaitre', 'trompette', 'surface', 'extension', 'listshowplatform', 'paradoxe', 'copyright', 'alliance', 'coeurs', 'ajoutes', 'bonus', 'increased', 'program', 'plot', 'treize', 'lack', 'englouti', 'destroyed', 'origins', 'talked', 'zeldas', 'inedites', 'justin', 'preapocalyptique', 'ajout', 'human', 'exclude', 'obligeant', 'obtenu', 'fait', 'deffets', 'innovations', 'race', 'empire', 'ajoute', 'lhistoire', 'impending', 'etre', 'instruction', 'standards', 'learn', 'amicalesquetes', 'rage', 'oiseau', 'arrows', 'titled', 'size', 'amene', 'conceived', 'soundtrack', 'quelques', 'connue', 'rogers', 'info', 'cities', 'vient', 'calvert', 'mario', 'actions', 'singleplayer', 'awakening', 'mechanic', 'versions', 'tenebres', 'montagne', 'temporel', 'console', 'expanded', 'mahardy', 'helpful', 'compose', 'concert', 'august', 'scattered', 'commercialisee', 'loresouls', 'gameplay', 'expired', 'retaining', 'active', 'tasked', 'rearranges', 'amelioration', 'future', 'inishie', 'boussole', 'translates', 'child', 'plupart', 'symphonic', 'andrew', 'nindb', 'network', 'used', 'deesses', 'tard', 'getting', 'dataforlag', 'bestselling', 'dores', 'majority', 'assume', 'donnant', 'ennemis', 'loccasion', 'registering', 'beloved', 'suffers', 'full', 'tells', 'hyrule', 'attempt', 'gamelon', 'varying', 'jouees', 'overview', 'partially', 'jeune', 'situant', 'cganimated', 'twilis', 'dynasty', 'koholint', 'fails', 'normal', 'california', 'haut', 'existent', 'developpeurs', 'talk', 'healththe', 'spot', 'occidentale', 'never', 'clairement', 'bellthe', 'dobjets', 'maintenant', 'mort', 'pointues', 'aquatiques', 'lessentiel', 'entered', 'leur', 'lorsquils', 'paying', 'west', 'certaines', 'filmworks', 'importante', 'david', 'facon', 'lyre', 'square', 'enters', 'faits', 'alimente', 'april', 'materials', 'receive', 'sest', 'niveaux', 'impacted', 'leau', 'predecesseurs', 'peripheral', 'telle', 'washington', 'donjons', 'siliconera', 'dimension', 'longtemps', 'zelda', 'including', 'lechange', 'ataru', 'license', 'quete', 'neal', 'most', 'fire', 'jardin', 'primordial', 'target', 'stupides', 'majora', 'emplis', 'ever', 'role', 'musicinspirationthe', 'machines', 'contre', 'includes', 'major', 'mark', 'difficulte', 'controlable', 'motives', 'mermusiquecette', 'vendue', 'embranchement', 'section', 'zeldalune', 'batterybacked', 'themes', 'faces', 'eponymous', 'failed', 'gamerankings', 'darknut', 'sounds', 'germany', 'kept', 'livrecrypte', 'highfantasy', 'voiceacted', 'pushpull', 'peace', 'dscrossoversthe', 'door', 'timethe', 'grosse', 'paralleles', 'regenerent', 'stop', 'wikipedia', 'rapide', 'etant', 'lexistence', 'todays', 'following', 'timeles', 'mature', 'converti', 'lineaire', 'litterature', 'laventure', 'publications', 'ventured', 'possess', 'gottliebs', 'played', 'mediavaliant', 'suivie', 'mention', 'consoles', 'entierement', 'laide', 'ailes', 'unique', 'dualscreen', 'highest', 'kokiris', 'novelist', 'secondaires', 'bonheur', 'semblait', 'every', 'controlling', 'soigner', 'wild', 'dorchestre', 'nimporte', 'heuristic', 'nayru', 'loses', 'arriver', 'exaucant', 'citing', 'animation', 'bibliographie', 'designer', 'pastnintendo', 'obtenir', 'uses', 'home', 'what', 'material', 'martin', 'parmi', 'clue', 'shall', 'lutte', 'lere', 'experimented', 'cloud', 'block', 'telechargement', 'retient', 'heart', 'shields', 'their', 'japanese', 'life', 'pointyeared', 'succes', 'convenableainsi', 'united', 'reflect', 'themed', 'chapter', 'coincide', 'celestia', 'mentioned', 'thoughts', 'gamesmain', 'cultivated', 'lives', 'meilleur', 'mogmas', 'timelimit', 'plan', 'gamesthroughout', 'century', 'laveu', 'plumes', 'cocorico', 'realistically', 'dsiware', 'princessfin', 'marines', 'musiquele', 'routes', 'loyalty', 'significant', 'motif', 'licensing', 'look', 'prominent', 'disparu', 'ingame', 'editors', 'competences', 'dailleurs', 'seasonsthe', 'garos', 'inclus', 'accepts', 'acceder', 'dooming', 'cotes', 'nommee', 'zeldale', 'meant', 'regular', 'enigme', 'purorogu', 'mielke', 'millions', 'remainocarina', 'rich', 'tels', 'semblables', 'contextsensitive', 'sonic', 'conserver', 'americaine', 'ones', 'edge', 'porting', 'utilisation', 'chateau', 'tester', 'website', 'unknown', 'award', 'legacy', 'tracey', 'appele', 'oregon', 'remake', 'connexe', 'egms', 'ensemble', 'order', 'joueren', 'bongos', 'personnages', 'chronology', 'reincarnation', 'discounted', 'decline', 'floating', 'commissioned', 'derivee', 'suellentrop', 'september', 'stealth', 'redevenu', 'melta', 'strength', 'brows', 'cavernes', 'complet', 'disembodied', 'triforce', 'malefique', 'livre', 'japonais', 'jouable', 'powerful', 'hope', 'ending', 'gardant', 'siecle', 'tournait', 'brett', 'manifests', 'colore', 'netait', 'album', 'episodesref', 'urbosa', 'amount', 'darunia', 'disambiguationloz', 'tingle', 'reveals', 'chronologies', 'simultanement', 'necessaire', 'descended', 'bros', 'says', 'genres', 'traversee', 'scene', 'episode', 'predominantly', 'ravel', 'paraduses', 'classic', 'creator', 'quality', 'franchises', 'petit', 'oriente', 'keys', 'japaneseonly', 'empechermangasune', 'topdown', 'responsesprincess', 'adaptations', 'tale', 'implicitly', 'advance', 'commence', 'chronologiquement', 'incarnations', 'jamess', 'classer', 'wiiannees', 'vingtcinq', 'plans', 'subject', 'titrant', 'chests', 'rejected', 'originale', 'vigilant', 'sortis', 'eiji', 'symphonie', 'dhyrule', 'phases', 'makuch', 'piano', 'elements', 'revelent', 'starting', 'franchiseafter', 'stylet', 'improve', 'exemple', 'crossovers', 'telling', 'north', 'bomb', 'pierres', 'celestiens', 'pasts', 'heroes', 'gamespy', 'souls', 'gave', 'quitter', 'world', 'similarities', 'swedish', 'referred', 'tete', 'along', 'cinq', 'voient', 'animearticle', 'granted', 'excepte', 'weapons', 'serieslinkmain', 'recompense', 'optimise', 'musictaking', 'variees', 'added', 'commun', 'arbre', 'multiple', 'permettent', 'battler', 'compositeur', 'airing', 'zeldanintendo', 'initially', 'akira', 'lieux', 'modifiee', 'medstroms', 'kennedy', 'twili', 'moindres', 'requiring', 'invisible', 'touche', 'printer', 'plots', 'adaption', 'antre', 'than', 'interactivity', 'dehors', 'company', 'ressemblent', 'revali', 'locked', 'pioneered', 'dune', 'discovery', 'joystiqcombrandon', 'adventurebattle', 'majoras', 'crossover', 'gives', 'deverrouiller', 'challenged', 'villain', 'existence', 'werent', 'four', 'bannies', 'fares', 'vetus', 'transformes', 'bows', 'pleasant', 'large', 'linked', 'exchanged', 'poeme', 'ranked', 'atmosphere', 'jose', 'away', 'merous', 'developpes', 'pose', 'already', 'donc', 'contemporary', 'namcos', 'dash', 'mont', 'additions', 'yells', 'pelland', 'barriere', 'tael', 'etres', 'volcanique', 'believes', 'producing', 'depicted', 'reedition', 'temporelle', 'secondhand', 'past', 'shorts', 'debloquer', 'guere', 'bombs', 'vision', 'gamebooks', 'chief', 'antagonist', 'show', 'portable', 'renvoie', 'laquelle', 'tutelle', 'depths', 'precieuses', 'posits', 'accomplish', 'shoemaker', 'lembleme', 'dedie', 'norris', 'minuscule', 'medias', 'ralliees', 'outsourced', 'fall', 'rencontrer', 'boomerangs', 'lumiere', 'dactionaventure', 'guide', 'greatest', 'sinspire', 'diffusion', 'jument', 'heros', 'opportunity', 'young', 'ayant', 'chart', 'unsourced', 'persistant', 'possibilite', 'figurine', 'octorocks', 'magical', 'download', 'radicalementthe', 'return', 'heavy', 'situated', 'amazoncom', 'fouille', 'mecanique', 'whole', 'navire', 'seconde', 'additional', 'enfanceprotection', 'artifacts', 'creed', 'newswire', 'hamano', 'seriesin', 'textures', 'zones', 'parer', 'aquatique', 'frame', 'residant', 'ocean', 'demon', 'figures', 'cree', 'chaque', 'fred', 'conteneur', 'explorations', 'strategic', 'differentes', 'mcwhertor', 'cagiva', 'tradition', 'lennemi', 'hyliens', 'saria', 'principaleimage', 'solo', 'effets', 'then', 'templesthe', 'alters', 'designed', 'periodically', 'possede', 'were', 'avril', 'affected', 'loriginalite', 'conferencelane', 'army', 'actually', 'coeur', 'freshlypicked', 'loosely', 'separate', 'specifique', 'pichlmair', 'monde', 'labyrinthes', 'warn', 'million', 'lexception', 'midi', 'dilesthe', 'claimed', 'device', 'sangliers', 'thought', 'primarily', 'certaine', 'ciela', 'batterie', 'completeness', 'share', 'balanced', 'general', 'shades', 'presents', 'episodes', 'power', 'franchissement', 'ishinomori', 'leading', 'subtitle', 'miyamotos', 'forts', 'messagemain', 'memorables', 'setting', 'rassemble', 'published', 'worthy', 'battles', 'page', 'hearts', 'incitation', 'forcenintendo', 'reflects', 'heads', 'winds', 'amazons', 'principal', 'reveal', 'cercueil', 'grandes', 'bring', 'demise', 'forbes', 'minijeux', 'poem', 'pieces', 'degree', 'indiscriminately', 'warp', 'left', 'accompagnee', 'milwaukie', 'habituelles', 'states', 'timecharacterssee', 'referenced', 'feature', 'shadow', 'lezard', 'offputting', 'boar', 'completely', 'allow', 'minute', 'marge', 'appears', 'utilite', 'presenter', 'annonce', 'gains', 'suffered', 'timemax', 'edition', 'printera', 'pages', 'celtique', 'perd', 'accrue', 'rise', 'puzzlebased', 'doiseaux', 'release', 'timeline', 'lors', 'peuples', 'hacheviande', 'resurrection', 'norrispinballcom', 'mondiale', 'controllable', 'molyneuxs', 'multijoueur', 'protagonists', 'something', 'best', 'reading', 'president', 'shortly', 'sujet', 'musicmaking', 'malediction', 'caverne', 'family', 'dialogue', 'combat', 'termina', 'sidon', 'destroy', 'wwwnintendocom', 'spirits', 'volcan', 'dabord', 'musiques', 'raison', 'minor', 'proceedings', 'march', 'emulated', 'campagnards', 'transition', 'wander', 'totalement', 'considerent', 'stay', 'forms', 'circuit', 'ceuxla', 'endroit', 'engine', 'magie', 'optimised', 'consistent', 'exposed', 'please', 'adding', 'manque', 'swordsthe', 'devoilees', 'replenish', 'laction', 'supervision', 'public', 'seraient', 'modification', 'individual', 'this', 'famille', 'find', 'pressing', 'screen', 'populations', 'locations', 'playersbreath', 'adapted', 'opus', 'dadopter', 'legacyaggregate', 'fable', 'sont', 'metroid', 'threats', 'statues', 'software', 'mystical', 'movies', 'detablir', 'humanity', 'adulthood', 'fighting', 'transportation', 'retains', 'humanoids', 'techradar', 'reperer', 'given', 'remaining', 'kingdom', 'effet', 'medolie', 'shooter', 'lakes', 'nindoricom', 'controler', 'graphical', 'continues', 'media', 'over', 'dexploration', 'deuxieme', 'sekiban', 'liberer', 'throughout', 'denlever', 'gerudos', 'green', 'vice', 'houser', 'ravels', 'relying', 'pokemon', 'milieux', 'petite', 'change', 'felonious', 'creating', 'sharon', 'climb', 'miniature', 'clef', 'base', 'difficultes', 'predestined', 'agahnim', 'nonjoueurs', 'followed', 'gained', 'especes', 'remakes', 'basant', 'interactive', 'sibyllin', 'pere', 'cible', 'debloque', 'wisdom', 'simply', 'make', 'bundled', 'techniques', 'daccomplir', 'ameliorant', 'received', 'prevue', 'spear', 'phil', 'picking', 'astro', 'february', 'xvother', 'habitaient', 'lhyrule', 'decided', 'working', 'dual', 'difficult', 'island', 'nouveaux', 'heroto', 'defeats', 'brian', 'tree', 'vejvoda', 'secretes', 'simplified', 'connu', 'triforcemis', 'these', 'them', 'oeuvre', 'toujours', 'placement', 'indicates', 'collectors', 'modified', 'didnt', 'lorule', 'cancelled', 'down', 'consumed', 'paradisenintendo', 'retrouve', 'total', 'amazon', 'pointed', 'include', 'deroulent', 'dated', 'protagonist', 'cartouches', 'zeldaan', 'retarder', 'diverses', 'totaka', 'darmani', 'principaleannees', 'uniques', 'garcon', 'scripted', 'kamiya', 'forming', 'dernier', 'balloon', 'witcher', 'matt', 'imagine', 'reprises', 'dobtenir', 'storytelling', 'kart', 'same', 'principalla', 'enemies', 'celui', 'features', 'sealed', 'gamescdi', 'refonte', 'timein', 'aonuma', 'royaumele', 'aussi', 'secraser', 'chaos', 'trouver', 'carquois', 'fourni', 'whose', 'scenario', 'secluded', 'reserver', 'beaten', 'adams', 'protecteurs', 'rare', 'formnintendo', 'quant', 'uphold', 'controle', 'between', 'lutilisation', 'open', 'dauteur', 'entrances', 'parallel', 'work', 'companies', 'kingdomthe', 'scaff', 'dreams', 'videogames', 'older', 'critics', 'differe', 'heavily', 'currently', 'late', 'vide', 'verte', 'poiscoms', 'propose', 'sacred', 'table', 'solid', 'allows', 'pattes', 'inconnu', 'laccueillir', 'penser', 'reception', 'remove', 'fight', 'portuguese', 'styled', 'mysterious', 'specific', 'peter', 'hatfield', 'remains', 'interpreted', 'party', 'countdown', 'swordjose', 'mute', 'itoi', 'series', 'fantasy', 'written', 'constant', 'takes', 'precedes', 'play', 'enfin', 'cris', 'outside', 'wiis', 'okami', 'whether', 'minimalist', 'bombe', 'zeldaen', 'utilisant', 'passent', 'inconsistencies', 'touffe', 'chemin', 'bookszelda', 'jupiter', 'navaient', 'second', 'scission', 'like', 'confidential', 'grey', 'backstory', 'subscription', 'sources', 'launch', 'neededin', 'receptacles', 'defeating', 'redirects', 'that', 'voyage', 'defeated', 'judge', 'meme', 'wiimotion', 'predecesseur', 'oceans', 'fairies', 'bosses', 'unlike', 'railroads', 'expirea', 'entrance', 'darksiders', 'actionorientedwhen', 'magician', 'votre', 'november', 'raconte', 'morceau', 'reel', 'realtime', 'cartridgessfour', 'recuperer', 'enlightenment', 'parsemes', 'worst', 'ricardo', 'paralyser', 'apparu', 'appreciee', 'provient', 'voleuses', 'brawl', 'woods', 'dont', 'disponible', 'wing', 'unostyled', 'constants', 'propre', 'baptisee', 'october', 'zeldazelda', 'became', 'localizing', 'secondesdurant', 'sommaire', 'cover', 'ganon', 'reborn', 'koeis', 'trouvera', 'onto', 'obtenue', 'choice', 'cave', 'forets', 'princesses', 'limited', 'feel', 'palais', 'origin', 'zeldasysteme', 'moblins', 'gamefaqs', 'gmbh', 'fame', 'territoire', 'souterrains', 'compte', 'zeldathemed', 'nexiste', 'oreilles', 'visible', 'live', 'troquer', 'name', 'leaps', 'parseme', 'sagissait', 'couleur', 'later', 'integralement', 'critically', 'scheduled', 'puissante', 'fulfilled', 'ganondorfs', 'devoile', 'passe', 'standalone', 'devie', 'vert', 'permet', 'oldest', 'reviewers', 'check', 'revealed', 'player', 'racing', 'minuscules', 'ziff', 'still', 'japonaise', 'voit', 'kingdomdengeki', 'dechapper', 'mostly', 'eddie', 'novembre', 'seek', 'deternels', 'launches', 'incomplete', 'recurring', 'colorbased', 'puis', 'ventes', 'rubis', 'fact', 'suspension', 'korean', 'questsin', 'press', 'catalogue', 'having', 'tassi', 'cdrom', 'significantly', 'commemorate', 'purchases', 'developpementau', 'colores', 'interact', 'those', 'commande', 'suivant', 'idea', 'text', 'monstrous', 'denigmes', 'accessible', 'triforcereeditions', 'primitive', 'virtuelle', 'organisee', 'first', 'parce', 'masques', 'walt', 'habitent', 'changement', 'transformer', 'massive', 'named', 'story', 'gold', 'donnent', 'missionnintendo', 'limage', 'reduced', 'demo', 'grab', 'animee', 'crunchyroll', 'reedites', 'videogame', 'shogakukan', 'etabli', 'ceux', 'containers', 'amerique', 'ligne', 'alors', 'vary', 'extra', 'organise', 'sybex', 'hobo', 'promotion', 'upcoming', 'zach', 'kain', 'quatre', 'largement', 'handheld', 'enjoyed', 'your', 'verrouille', 'sagesneil', 'invades', 'mangas', 'inexistants', 'makes', 'design', 'apparaissant', 'ressusciter', 'cartoon', 'ported', 'supplementaires', 'apparaissent', 'more', 'broadcast', 'combataudiokoji', 'memorable', 'passage', 'visage', 'timelong', 'kohler', 'souvenir', 'production', 'hylia', 'videoles', 'multidirectional', 'controller', 'seuls', 'quickly', 'coordinating', 'truly', 'latest', 'saga', 'battre', 'cited', 'spirit', 'card', 'yunobo', 'passee', 'strong', 'vaati', 'sleeping', 'daniel', 'potential', 'ouvert', 'essentiellement', 'semblable', 'perfect', 'kondoplatforms', 'proved', 'expansion', 'result', 'believing', 'average', 'protegee', 'established', 'club', 'camera', 'payants', 'egalement', 'silent', 'together', 'marksmanship', 'begins', 'setendant', 'bienvenue', 'paralleledefaite', 'avait', 'rend', 'guardians', 'soupe', 'titles', 'securing', 'iasig', 'hormis', 'audessus', 'thousands', 'skull', 'bras', 'core', 'contained', 'amicales', 'middle', 'escaping', 'ladaptation', 'faisant', 'decouvrir', 'near', 'cartes', 'importantes', 'manager', 'credithugh', 'officiellement', 'objets', 'melange', 'aided', 'exemplaires', 'ledification', 'metacriticthe', 'nintendocom', 'campagne', 'studio', 'phare', 'dernieres', 'eight', 'speaks', 'labrynna', 'dordinn', 'eoliens', 'grottes', 'contient', 'suggera', 'temples', 'intelligents', 'want', 'finalement', 'friday', 'locarina', 'western', 'ability', 'riju', 'limitations', 'divers', 'bateau', 'complete', 'sidescrolling', 'compagnons', 'information', 'dragon', 'been', 'scoring', 'remastering', 'departing', 'autrement', 'pris', 'npcs', 'environmental', 'villagesmais', 'today', 'chose', 'humanoide', 'tourne', 'jeuarticle', 'tetra', 'mowatt', 'manier', 'loup', 'chef', 'limitees', 'detaille', 'timelines', 'half', 'varied', 'start', 'leitmotifs', 'ways', 'expressed', 'jack', 'resting', 'noting', 'issus', 'vend', 'toki', 'hors', 'contes', 'settings', 'utilisee', 'addition', 'occur', 'papillons', 'taller', 'poor', 'interview', 'trendsmcwhertor', 'inspired', 'termes', 'mediaworks', 'movement', 'commercialserie', 'emphasize', 'hidetaka', 'instead', 'brigands', 'ereadercancelled', 'template', 'suivants', 'combattent', 'rumeur', 'empli', 'miroir', 'theft', 'temps', 'multiplayer', 'ambulants', 'individuals', 'gottlieb', 'murmured', 'from', 'tezukacomposers', 'ambience', 'nouveau', 'font', 'convergence', 'generalement', 'graphics', 'kayas', 'laccessoire', 'kara', 'cocottes', 'ashcraft', 'realmin', 'doreenintendo', 'caracterisees', 'envahit', 'voir', 'saint', 'hidden', 'commonly', 'developed', 'boat', 'disneys', 'carte', 'enemiesthe', 'abandonne', 'explored', 'acquis', 'dreamfictional', 'portion', 'gamesradar', 'mythology', 'known', 'voix', 'performances', 'celshading', 'gamecube', 'rendent', 'hajime', 'dans', 'cartridge', 'hideki', 'password', 'lovely', 'mianimale', 'collection', 'warping', 'ecrit', 'dixneuf', 'jamais', 'barcode', 'flagship', 'according', 'mythologiques', 'minimal', 'kidnapping', 'digra', 'list', 'hundred', 'reverse', 'anthropomorphic', 'divinity', 'nakatsuka', 'continued', 'proposer', 'perhaps', 'steeped', 'site', 'domination', 'zapper', 'shows', 'sort', 'coups', 'product', 'vingt', 'said', 'kind', 'differente', 'contrepartie', 'interacting', 'doivent', 'report', 'grant', 'crypte', 'executive', 'modifications', 'ruines', 'labyrinthine', 'densetsu', 'realisee', 'dessus', 'mauvaise', 'winfried', 'followup', 'seal', 'outre', 'actual', 'americanotes', 'offert', 'goddess', 'cracheurs', 'demonstration', 'kill', 'clarified', 'right', 'lanterne', 'smash', 'decembre', 'lien', 'prince', 'princessen', 'devinrent', 'which', 'princesse', 'qualite', 'gameepisode', 'tokays', 'disappearing', 'consideree', 'clefs', 'essaye', 'celesbourg', 'repaire', 'napparait', 'much', 'linstant', 'blood', 'view', 'foret', 'rearranged', 'rapidement', 'fourth', 'incluent', 'help', 'triforces', 'parallele', 'passed', 'croit', 'dorees', 'slashstyle', 'cardscanning', 'popularity', 'centres', 'stone', 'deku', 'liens', 'abilities', 'lecteur', 'replenished', 'sands', 'arriere', 'forever', 'peche', 'trouves', 'spaceworld', 'regroupant', 'collaborations', 'augmente', 'american', 'transformee', 'craig', 'sils', 'entier', 'studios', 'insuffisamment', 'gagner', 'lopus', 'capacites', 'commander', 'customers', 'using', 'gamerscom', 'nourriture', 'wide', 'timenintendo', 'deviendra', 'tragedy', 'digital', 'magique', 'vendus', 'raccourcis', 'supercontinent', 'officielle', 'picross', 'magic', 'assez', 'comes', 'dire', 'nearly', 'hyliennes', 'depuis', 'person', 'taya', 'accompagne', 'openingsa', 'incarnation', 'essays', 'formant', 'toute', 'went', 'recurrents', 'memes', 'movie', 'gamepad', 'animaux', 'compares', 'swordin', 'acknowledged', 'lands', 'principaux', 'instance', 'status', 'whereas', 'extend', 'completement', 'satellaviews', 'grands', 'gerudo', 'offjonti', 'suggestion', 'navigating', 'youth', 'reprenant', 'annexe', 'taking', 'websites', 'conduisant', 'rockstar', 'reunite', 'independants', 'comprising', 'genre', 'aggregator', 'column', 'mais', 'fragments', 'passwords', 'rares', 'contrat', 'springs', 'pour', 'dikana', 'producer', 'needed', 'prior', 'deroules', 'embodies', 'allplunkett', 'secret', 'hints', 'took', 'listed', 'rankings', 'tuer', 'melodies', 'derniere', 'exceptions', 'although', 'mihommes', 'surprise', 'revela', 'simultaneously', 'mojo', 'setant', 'travail', 'iria', 'elle', 'relique', 'clear', 'archived', 'mipha', 'came', 'ultimate', 'review', 'dexemplaires', 'chevauchent', 'encore', 'even', 'dautre', 'mauvais', 'technology', 'bookta', 'tests', 'davis', 'such', 'decouverte', 'mots', 'zerudanochuanshuo', 'scaled', 'does', 'citizen', 'grezzopublishers', 'farore', 'jawdropping', 'maniere', 'communs', 'navi', 'disambiguationthe', 'vitality', 'ornee', 'vaste', 'screwattacks', 'chain', 'europeen', 'altered', 'deblaye', 'reviews', 'maximale', 'mitch', 'nearby', 'langley', 'highestrated', 'resolu', 'theme', 'dispose', 'speculated', 'whitehead', 'article', 'periode', 'foreground', 'worlds', 'artwork', 'versa', 'morceaux', 'confirme', 'heartthe', 'antagonists', 'audela', 'years', 'hardware', 'sept', 'nouvelles', 'grappin', 'gamesthe', 'through', 'experiences', 'tommy', 'quelquesuns', 'historique', 'types', 'progressing', 'femelles', 'tmnt', 'special', 'dessine', 'modes', 'totalite', 'seriesthree', 'goodfellas', 'peuplent', 'publishing', 'another', 'essentiel', 'important', 'echoue', 'zeldaaccording', 'generation', 'yuichi', 'concepteurs', 'hylian', 'travel', 'melee', 'maurice', 'remote', 'stricte', 'eaux', 'next', 'moderne', 'fini', 'graphismes', 'color', 'implique', 'serieshearing', 'unnamed', 'informer', 'orchestra', 'retail', 'difficiles', 'elles', 'outstanding', 'masque', 'cent', 'chevaliers', 'profil', 'month', 'notamment', 'minimum', 'timecest', 'inspiration', 'remnants', 'principalement', 'servir', 'ganondorf', 'takizawa', 'contains', 'apparait', 'controlled', 'telechargeable', 'cours', 'arcade', 'backstories', 'dassener', 'changer', 'physically', 'parties', 'expansive', 'prevu', 'prequelle', 'exploree', 'kyoto', 'particularites', 'visant', 'instruments', 'stories', 'current', 'deviennent', 'points', 'cancel', 'culture', 'tribute', 'adventures', 'potion', 'chronicles', 'monture', 'principles', 'proposes', 'hesite', 'showing', 'cependant', 'accueil', 'armes', 'guitare', 'have', 'conception', 'dstyled', 'premier', 'thirst', 'ledition', 'jeule', 'well', 'citations', 'americain', 'previous', 'fantastique', 'rapprochant', 'handicapant', 'siecles', 'concept', 'creation', 'tunic', 'refinements', 'needing', 'cartridges', 'uncharted', 'dunites', 'informations', 'roberts', 'bloodline', 'consolesocarina', 'encyclopediathis', 'wilds', 'taupes', 'gamespot', 'marpo', 'legend', 'landsettingmain', 'lacoste', 'aventure', 'knight', 'precedent', 'death', 'nouvel', 'combining', 'welsh', 'revele', 'successful', 'called', 'people', 'vendues', 'association', 'wear', 'dexcellents', 'flaming', 'vaincu', 'toutefois', 'magazine', 'released', 'reedite', 'both', 'film', 'editions', 'exposition', 'further', 'explorer', 'couleurs', 'panlink', 'trailer', 'fast', 'michael', 'dhyrulearticle', 'except', 'apparaitre', 'polygon', 'connected', 'desktops', 'continuation', 'facteur', 'guinness', 'utilise', 'teleporteurs', 'master', 'gamesat', 'nothing', 'trap', 'everimpactmultiple', 'contain', 'unes', 'subrosia', 'musical', 'lawshigeru', 'disque', 'fantomatiques', 'okamoto', 'progress', 'video', 'limite', 'descendance', 'quests', 'speaking', 'porter', 'koji', 'penetrer', 'diverted', 'annoncerent', 'pestes', 'vent', 'japon', 'acces', 'quun', 'letre', 'introduced', 'wildmarch', 'offer', 'legendary', 'each', 'saisons', 'righthanded', 'titre', 'towns', 'premiere', 'will', 'orchestrated', 'however', 'tous', 'composition', 'represented', 'environnement', 'black', 'exclusively', 'captain', 'hysteria', 'recorder', 'announcement', 'restored', 'connecting', 'accepted', 'defait', 'larme', 'resoudre', 'bourse', 'invertebres', 'lorsquil', 'coming', 'foretoldshigeru', 'commercial', 'concerts', 'seasons', 'exclusives', 'fevrier', 'crossbow', 'fate', 'attack', 'told', 'vaincre', 'precision', 'tetras', 'universe', 'aliases', 'enabling', 'leader', 'emparer', 'village', 'suivantes', 'week', 'aspects', 'training', 'pack', 'sonores', 'experience', 'succeed', 'teased', 'because', 'soixantedouze', 'swordlors', 'progresses', 'infamous', 'jour', 'dates', 'islandfilled', 'rouge', 'appeles', 'enfancele', 'lead', 'shop', 'curse', 'zeruda', 'oppose', 'troisieme', 'doorways', 'enough', 'comfortable', 'shinbun', 'personnes', 'differents', 'retranscrits', 'dadresse', 'ganonplus', 'print', 'flows', 'reelle', 'inhabitants', 'microsoft', 'brilliant', 'arise', 'fran', 'gods', 'mythologie', 'relative', 'either', 'flag', 'enigmes', 'function', 'wakerthe', 'gorons', 'lapparence', 'crepuscule', 'designing', 'villages', 'sounded', 'answer', 'tell', 'seigneur', 'chronologie', 'planning', 'splits', 'contrairement', 'characters', 'appris', 'presente', 'america', 'enacted', 'chacun', 'confirma', 'audience', 'connut', 'debut', 'mivegetale', 'apparus', 'example', 'lumineuse', 'disagreed', 'proceeding', 'contents', 'also', 'become', 'stated', 'himself', 'chasseurs', 'debate', 'lifespan', 'earth', 'hyrulian', 'possedees', 'limportance', 'fictional', 'downloadable', 'integrated', 'found', 'boomerang', 'foule', 'question', 'arms', 'revanche', 'wont', 'monopoly', 'restore', 'july', 'principale', 'piafs', 'zeldafebruary', 'soul', 'confirmed', 'puisque', 'taquinees', 'oracle', 'within', 'obtain', 'ages', 'milodon', 'joueurs', 'employee', 'particularly', 'fitzgeraldganonmain', 'apres', 'virtual', 'neil', 'boite', 'means', 'gamepro', 'angeles', 'some', 'zeldafrom', 'bolero', 'entirely', 'takashi', 'female', 'novel', 'inchange', 'protection', 'battling', 'paul', 'wish', 'tracksin', 'staff', 'baba', 'larbre', 'independently', 'nest', 'slowly', 'evolutions', 'laterreleased', 'particulier', 'narratif', 'deviation', 'creusant', 'guides', 'essayant', 'blobs', 'parodies', 'hero', 'objectives', 'popfiction', 'single', 'categories', 'annoncee', 'seasonprint', 'choppier', 'symphony', 'precommande', 'exelo', 'roleplaying', 'better', 'nintendos', 'ocarina', 'ends', 'aide', 'ranks', 'limitee', 'moon', 'part', 'elfes', 'line', 'famicom', 'surrounding', 'knitted', 'toon', 'certains', 'perspective', 'egos', 'donjonsarticle', 'heartbased', 'subsequent', 'different', 'triangles', 'disc', 'trois', 'produced', 'linking', 'star', 'dherbe', 'numerises', 'divinites', 'completing', 'liveaction', 'retrouver', 'quelque', 'cranes', 'accordait', 'cela', 'inside', 'rural', 'animated', 'lindustrie', 'explorereception', 'lage', 'locating', 'ocarinas', 'rennes', 'merely', 'favorite', 'projekt', 'reality', 'serve', 'ztargeting', 'serieconsole', 'sequels', 'conjunction', 'dynamics', 'link', 'joues', 'exception', 'central', 'emblem', 'episodespendant', 'directement', 'ainsi', 'royal', 'enfance', 'content', 'serieslcd', 'repurpose', 'marque', 'epona', 'linterieur', 'logique', 'vivant', 'rupee', 'prophecy', 'gaiden', 'josh', 'derouler', 'tour', 'spirituel', 'confondre', 'daruk', 'vaincus', 'difference', 'kodai', 'rang', 'puzzlesolving', 'take', 'firone', 'supporting', 'describing', 'fumito', 'theyve', 'tout', 'tikwis', 'vendu', 'reliee', 'featured', 'employed', 'steal', 'impressions', 'contexts', 'becensabot', 'mediatv', 'segment', 'skyloft', 'bundle', 'holodrum', 'lantern', 'captured', 'thereafter', 'announces', 'lunivers', 'retour', 'withstand', 'placing', 'sweden', 'soleil', 'widespread', 'viacom', 'glenn', 'vivent', 'recordsle', 'coffres', 'magasin', 'walton', 'immortal', 'moteur', 'morts', 'princess', 'candleocarina', 'signe', 'scullion', 'sonobe', 'hesitation', 'tracksthe', 'peuvent', 'atteindre', 'tabata', 'crackedcomnorris', 'semaines', 'warrior', 'trame', 'wessel', 'darkness', 'creees', 'laerouage', 'mesure', 'representes', 'chronologiea', 'readied', 'ganons', 'villains', 'sous', 'present', 'thing', 'artifact', 'document', 'books', 'quetes', 'jusqua', 'terre', 'intitule', 'derivesdessin', 'meets', 'esprits', 'sets', 'placed', 'molyneux', 'departure', 'fromsoftware', 'forced', 'tezuka', 'centers', 'hourglass', 'accessibles', 'june', 'might', 'motionplus', 'developper', 'permettraient', 'particularite', 'arthurian', 'spinoff', 'mechanics', 'avaient', 'sold', 'quil', 'monstres', 'puzzles', 'seen', 'gamecubecitation', 'year', 'needs', 'ozaki', 'cite', 'leurs', 'division', 'while', 'queue', 'must', 'etaient', 'rooms', 'insere', 'reversed', 'aujourdhui', 'adulte', 'events', 'premiers', 'lepee', 'plaine', 'failure', 'offre', 'grezzo', 'aggregate', 'hillsides', 'utiliser', 'smaller', 'sorte', 'differently', 'offered', 'combats', 'cycle', 'americana', 'able', 'overarching', 'unlock', 'memory', 'habite', 'sequel', 'lediteur', 'approach', 'being', 'proche', 'online', 'profite', 'monsters', 'nikkan', 'obtained', 'toymax', 'straightforward', 'expanding', 'himekawa', 'tingles', 'kazumi', 'element', 'semparer', 'directe', 'lile', 'shield', 'provided', 'created', 'extensive', 'comics', 'farted', 'precedents', 'lars', 'excalibur', 'tient', 'soit', 'cocolint', 'animal', 'exploration', 'everything', 'rouler', 'super', 'servent', 'daction', 'lorsque', 'timebased', 'receiving', 'encyclopedia', 'january', 'shotaro', 'progresser', 'humain', 'disk', 'pologne', 'inclut', 'autre', 'mixture', 'septemberlimited', 'doreilles', 'rendered', 'magazines', 'times', 'summer', 'dosados', 'paysil', 'humaine', 'sans', 'believed', 'australia', 'afin', 'anciens', 'officially', 'good', 'zoras', 'indiquant', 'when', 'holder', 'founder', 'pendant', 'introduit', 'rosy', 'appearing', 'nordique', 'longues', 'depossedee', 'humanoid', 'rongeurs', 'montre', 'mondeocean', 'celuici', 'location', 'stars', 'enemy', 'minishs', 'industry', 'computeranimated', 'pouvoir', 'echanger', 'prochain', 'solving', 'senrichit', 'secondairesimage', 'remakesnintendo', 'ressuscite', 'details', 'prosperity', 'enix', 'appearance', 'naughty', 'pinball', 'erafennec', 'existed', 'multijoueurversions', 'lorion', 'seriess', 'imperium', 'holds', 'score', 'donnes', 'gamesas', 'hytopia', 'capacityboard', 'maybe', 'rewarded', 'crossing', 'accompagnes', 'chez', 'fleurs', 'relives', 'multiples', 'aired', 'port', 'nintendocreators', 'centre', 'environnant', 'symboles', 'considerablement', 'arielle', 'litteralement', 'exploring', 'fruition', 'celshaded', 'music', 'various', 'spoken', 'doom', 'lists', 'annual', 'avoided', 'george', 'nordamericaine', 'choisi', 'wand', 'poules', 'retrieved', 'interaction', 'copie', 'oeufs', 'equipment', 'diles', 'seriesa', 'opposed', 'metacritic', 'profit', 'systeme', 'possedent', 'petites', 'detaillee', 'mipoissons', 'retained', 'kollar', 'verts', 'stereoscopic', 'format', 'doree', 'waker', 'manchots', 'zeldamain', 'nondance', 'focusing', 'fils', 'lite', 'cinematiquesdautres', 'etatsunis', 'testeurs', 'jourla', 'removed', 'realise', 'images', 'influence', 'hostiles', 'learns', 'incluse', 'dingo', 'zeldathe', 'side', 'manual', 'prisonniers', 'bouclier', 'scenarios', 'mishouzaki', 'performed', 'form', 'enterprises', 'berghammer', 'situe', 'considered', 'brief', 'suite', 'masks', 'consolethe', 'lemploi', 'library', 'abattu', 'anime', 'simplement', 'toutes', 'considere', 'prize', 'tresors', 'famicoms', 'jeux', 'nelsonic', 'montagnes', 'roster', 'require', 'dengeki', 'platinum', 'games', 'essential', 'dexperience', 'reussie', 'dungeon', 'paradise', 'wolfpromotional', 'complicated', 'fully', 'droit', 'midona', 'dark', 'rallient', 'crossedover', 'tenue', 'aurait', 'certain', 'gamesindustry', 'genta', 'copy', 'vividlyrealised', 'crystal', 'productions', 'creations', 'representant', 'chestin', 'bonnet', 'generations', 'normale', 'incorporates', 'kondo', 'warriors', 'lautre', 'embrace', 'vestal', 'reorchestrees', 'days', 'audio', 'focuses', 'marchand', 'bourgeon', 'under', 'tallarico', 'zeldatotilo', 'kozuo', 'jason', 'select', 'alexander', 'identity', 'objet', 'lying', 'canonmain', 'entre', 'expulsees', 'doreesannees', 'baguette', 'lesprit', 'etoiles', 'entries', 'sequence', 'composer', 'nesthe', 'inedit', 'pointu', 'royaume', 'free', 'kondokoji', 'vegetale', 'horse', 'developpement', 'mcdonald', 'poulpes', 'temple', 'quils', 'birth', 'rescuing', 'collector', 'included', 'fights', 'motifs', 'poured', 'mouths', 'selling', 'reputes', 'hyrules', 'powers', 'selon', 'turnbased', 'itself', 'title', 'plastic', 'stephen', 'subrosiens', 'just', 'usually', 'seule', 'graphiquement', 'optionalfour', 'noted', 'third', 'praised', 'mobygames', 'decide', 'adult', 'contenant', 'japans', 'correspond', 'larc', 'historia', 'soulcalibur', 'japonle', 'attaque', 'paralyze', 'textbook', 'rest', 'place', 'nintendo', 'marvel', 'notes', 'secrets', 'lance', 'comporte', 'verification', 'perilmais', 'wife', 'influenced', 'here', 'confere', 'beaucoup', 'mike', 'marchands', 'possedant', 'platinumgames', 'comment', 'copies', 'logo', 'despite', 'nombre', 'crucial', 'enabled', 'michemin', 'lionhead', 'transform', 'horrifying', 'voice', 'canada', 'trackers', 'ready', 'exactement', 'senses', 'souhaitent', 'seven', 'serieemblemeles', 'move', 'eshop', 'triangle', 'travers', 'across', 'defeat', 'alternate', 'nonplayer', 'relic', 'sauver', 'subscribing', 'capture', 'identify', 'renewing', 'forme', 'lannee', 'booklet', 'centuries', 'vastes', 'doiseau', 'janvier', 'duel', 'mouvements', 'sends', 'imagination', 'instrument', 'explication', 'percevoir', 'inspire', 'todd', 'nord', 'grand', 'maskthe', 'dungeons', 'task', 'connues', 'influenceevery', 'need', 'tues', 'gouverner', 'chili', 'realm', 'impa', 'ancient', 'spike', 'built', 'faroriaennemisimage', 'ville', 'east', 'often', 'films', 'chosen', 'shown', 'reactions', 'allowing', 'item', 'lieu', 'button', 'feelings', 'deplacement', 'voire', 'unproduced', 'garden', 'shigeru', 'maison', 'entire', 'livres', 'disponibles', 'hyrulean', 'speciales', 'knows', 'europe', 'mabinogion', 'medievale', 'approfondissant', 'sablier', 'protect', 'peut', 'femme', 'bien', 'sages', 'dite', 'three', 'celestriers', 'dealing', 'nait', 'descendants', 'lockon', 'predecessor', 'recoit', 'connect', 'identique', 'contraignant', 'commercially', 'filmsin', 'tant', 'dotee', 'meter', 'mini', 'others', 'miniboss', 'persia', 'returns', 'ciel', 'grunts', 'monster', 'hante', 'seriesmain', 'entouree', 'sauve', 'virtues', 'downloads', 'located', 'stalfos', 'habitant', 'portrayed', 'eighth', 'remaster', 'canon', 'videos', 'venerable', 'avatar', 'monnaie', 'history', 'personnalise', 'becoming', 'developer', 'ganonganon', 'yoshiki', 'marquant', 'tyrant', 'confirmee', 'espece', 'switch', 'note', 'vieslieuximage', 'silvestre', 'cohabiter', 'tournant', 'studies', 'anniversary', 'transforme', 'purpose', 'spacey', 'vanpool', 'avant', 'level', 'final', 'hatred', 'assist', 'petits', 'ressemble', 'theorie', 'otherwiseimpassable', 'reeditions', 'francaise', 'acclaim', 'sell', 'quune', 'eternally', 'lentree', 'always', 'bloodsoaked', 'amicaux', 'exclusive', 'gaming', 'aneantir', 'campaign', 'seulement', 'legendes', 'troublesome', 'darker', 'widely', 'electronic', 'brilliance', 'mygames', 'souvent', 'cable', 'graphique', 'tres', 'perform', 'awarded', 'pourtant', 'reunited', 'sylvestre', 'originally', 'purchasing', 'doute', 'annexes', 'cieux', 'avancee', 'radio', 'reason', 'great', 'difficile', 'contraint', 'novateur', 'epoque', 'donner', 'publiee', 'based', 'cette', 'categorie', 'control', 'multitude', 'wanted', 'learned', 'orchestral', 'humains', 'fans', 'sword', 'playable', 'impact', 'propres', 'parts', 'explained', 'motionblur', 'small', 'manette', 'character', 'regions', 'corps', 'lechec', 'exemplairesla', 'torres', 'actionquand', 'last', 'cartoons', 'cultures', 'recherche', 'consists', 'involve', 'macdonald', 'produits', 'golden', 'wired', 'gamesclarification', 'aroo', 'archway', 'creatures', 'predecessors', 'split', 'integre', 'nombreuses', 'calibur', 'natural', 'exploits', 'follow', 'jouer', 'ultimately', 'profile', 'vegetaux', 'before', 'several', 'frequently', 'rolling', 'auto', 'raphael', 'critiques', 'boule', 'seriesfollowing', 'tracks', 'huit', 'kayali', 'wind', 'peters', 'news', 'blocked', 'griseocarina', 'disposition', 'perdus', 'gameboy', 'showed', 'unlockable', 'tinker', 'vers', 'accrues', 'linkproduits', 'main', 'luke', 'available', 'solely', 'paru', 'sousboss', 'kokiri', 'hylians', 'battle', 'plague', 'cast', 'reconnaitre', 'book', 'joueurthe', 'cartouche', 'converted', 'during', 'privee', 'kotaku', 'cologne', 'veut', 'franchise', 'arrangement', 'ancestors', 'journey', 'bombes', 'pourrait', 'bulbins', 'service', 'should', 'publication', 'mailed', 'juin', 'mixing', 'very', 'droits', 'ames', 'lexpansion', 'dessai', 'handed', 'screwattack', 'avoir', 'ombre', 'levels', 'milieu', 'biggoron', 'layouts', 'moyens', 'reveille', 'paysage', 'felt', 'lloyd', 'caledfwlch', 'targeting', 'subsequently', 'devient', 'contentant', 'apparence', 'trilogie', 'chris', 'shards', 'xplay', 'goddessnintendo', 'concentre', 'engloutie', 'fees', 'menacing', 'producers', 'gros', 'struggle', 'avance', 'director', 'upon', 'rocheux', 'neededa', 'princessin', 'fighter', 'souligner', 'marais', 'divine', 'egares', 'acheter', 'allowed', 'entry', 'anniversaire', 'board', 'range', 'deux', 'statements', 'sentient', 'wolf', 'hall', 'five', 'entertainment', 'feminin', 'factorydans', 'cyberpunk', 'seed', 'inhouse', 'communication', 'trip', 'threat', 'mode', 'characteristically', 'resides', 'originaires', 'voler', 'imagi', 'ressemblant', 'loriens', 'lextension', 'back', 'baton', 'upcom', 'creee', 'turnnintendo', 'disparition', 'goddesses', 'connection', 'geography', 'pete', 'deep', 'empecher', 'shrink', 'appear', 'search', 'forwards', 'announced', 'feter', 'standing', 'dhyrulehistorique', 'presumably', 'lacquisition', 'with', 'mirror', 'publies', 'sense', 'autour', 'rire', 'univers', 'bleules', 'epee', 'ueda', 'faire', 'tornade', 'tokyo', 'affixed', 'moving', 'plays', 'born', 'renforce', 'appelee', 'modifie', 'avoid', 'rides', 'caracteristiques', 'changing', 'since', 'flowers', 'original', 'long', 'fairy', 'digitally', 'kamigami', 'containing', 'luimeme', 'hiatus', 'adaptation', 'whalen', 'hommage', 'ashes', 'references', 'lave', 'trigger', 'remaniement', 'entrainant', 'land', 'recurrent', 'stage', 'reliable', 'forward', 'revamped', 'terrains', 'fantome', 'niveau', 'system', 'user', 'fell', 'unusnzleusazeldas', 'unchanged', 'primaire', 'train', 'transformed', 'focused', 'dementi', 'creature', 'save', 'chronologythe', 'agressivite', 'symphoniquepour', 'zonedans', 'bearers', 'game', 'wants', 'populaire', 'fiveyear', 'technique', 'assemblages', 'harris', 'traversees', 'rereleases', 'they', 'pahya', 'reportmcmillan', 'dapparence', 'importants', 'gannett', 'sagesse', 'reprise', 'parfois', 'lexploration', 'watch', 'competitionas', 'serieen', 'again', 'selfcontained', 'canceledbefore', 'sorti', 'pres', 'incentive', 'label', 'derives', 'indispensables', 'actionaventure', 'legende', 'pouvait', 'creant', 'croyant', 'cote', 'immense', 'coquillages', 'moins', 'presque', 'tower', 'alchimie', 'tribu', 'links', 'grises', 'edite', 'omnipotent', 'cest', 'resume', 'rebuild', 'slightly', 'satoru', 'tablets', 'aller', 'ancestrales', 'entirety', 'brad', 'europethe', 'disappointed', 'continue', 'facilement', 'precise', 'premieres', 'forteresse', 'realiste', 'shockers', 'uhors', 'wildlors', 'force', 'deity', 'insert', 'presse', 'proof', 'remainder', 'utiles', 'influences', 'existe', 'comble', 'davies', 'peuple', 'where', 'advice', 'inconnue', 'difficulty', 'sagit', 'londres', 'spectre', 'dutton', 'otero', 'after', 'introduction', 'zeldaprincess', 'sought', 'korogus', 'melodic', 'remained', 'systemfirst', 'only', 'shading', 'publie', 'boss', 'breaks', 'realisme', 'oeuvres', 'many', 'piece', 'samus', 'seventhgreatest', 'partir', 'mido', 'handled', 'fechner', 'docarina', 'seeks', 'sales', 'linteret', 'precarious', 'ennemies', 'doit', 'detailed', 'plotline', 'ended', 'scores', 'savoir', 'diffusees', 'december', 'theres', 'partie', 'septembre', 'combattre', 'zeldapour', 'crushed', 'minish', 'nuages', 'quocarina', 'though', 'areas', 'capcom', 'relativement', 'once', 'vivre', 'heures', 'releases', 'twilight', 'portal', 'british', 'mirrored', 'light', 'there', 'ubisoft', 'doresla', 'drops', 'joueur', 'perche', 'disposant', 'external', 'tires', 'reussi', 'roles', 'designers', 'zeldalink', 'discarding', 'changed', 'mask', 'donjongeneralement', 'problematique', 'footage', 'comme', 'publisher', 'bois', 'existsince', 'quest', 'exterieurcaverne', 'photo', 'reaver', 'ronaghan', 'celle', 'actuels', 'autant', 'distributed', 'charactersin', 'etait', 'represente', 'interagissent', 'ailleurs', 'semble', 'demployer', 'courage', 'tunique', 'facile', 'swordplay', 'pause', 'guardian', 'dedicated', 'wayne', 'rate', 'monthly', 'comprenant', 'planned', 'troubles', 'zone', 'doors', 'rendre', 'phantom', 'double', 'produite', 'connait', 'titres', 'doreetous', 'intervenir', 'action', 'lombre', 'previously', 'teleportation', 'borrowed', 'allumniation', 'preorder', 'commercialise', 'poorly', 'sometime', 'birthday', 'flute', 'thomas', 'parti', 'evil', 'devait', 'replaced', 'hennig', 'specialises', 'auparavant', 'pushed', 'traditional', 'boken', 'earliest', 'made', 'quelle', 'maskle', 'give', 'isbn', 'locales', 'playing', 'respectivelyin', 'ezlo']
wordlist = []
for i in tmpwordlist:
     if not i.lower() in wordlist:
          wordlist.append(i.replace(" ","").lower())

def baseSystemTobaseN(n,outputBaseSymbols):    
    base = len(outputBaseSymbols)-1
#    print(base)
#    print(outputBaseSymbols)
    #base = 26
    num = []
    while True:
        q = n//base
        r = n % base
        num.append(r)
        n = q
        if q < base:
            num.append(q)
            break
    return ''.join([outputBaseSymbols[x] for x in num[::-1]])

def toSystemBase(s,inputBaseSymbols):
    base = len(inputBaseSymbols)   
    result = 0
    for i,j in enumerate(s[::-1]):
        result += inputBaseSymbols.index(j)*pow(base,i)
    return result

def baseXtoY(source,inputBaseSymbols,outputBaseSymbols):
    return baseSystemTobaseN(
             toSystemBase(source,inputBaseSymbols),
             outputBaseSymbols )


def baseSystemTobaseN2(n,outputBaseSymbols):
    #base = 26
    base = len(outputBaseSymbols)
    num = []
    while True:
        q = n//base
        r = n % base
        num.append(r)
        n = q
        if q < base:
            num.append(q)
            break
    return ''.join([outputBaseSymbols[x] for x in num[::-1]])

def toSystemBase2(s,inputBaseSymbols):
    base = len(inputBaseSymbols)
    result = 0
    for i,j in enumerate(s[::-1]):
        result += inputBaseSymbols.index(j)*pow(base,i)
    return result

def baseXtoY2(source,inputBaseSymbols,outputBaseSymbols):
    return baseSystemTobaseN2(
             toSystemBase2(source,inputBaseSymbols),
             outputBaseSymbols )


def leet(txt):
     txt = txt.lower()
     txt = txt.replace("a","4").replace("b","8").replace("e","3").replace("g","6").replace("i","1").replace("l","1").replace("m","44").replace("o","0").replace("q","9").replace("r","|2").replace("s","5").replace("t","7").replace("z","2")
     return txt.upper()

def leet2(txt):
     txt = txt.lower()
     txt = txt.replace("a","4").replace("b","8").replace("e","3").replace("g","6").replace("i","1").replace("l","1").replace("o","0").replace("s","5")
     return txt.upper()


def A1Z26Cipher ( code ):
    return " ".join(
        ["".join([((re.search("\D", c).group(0)).join(
            [(chr(int(i)-1+ord('A'))) if i.isdigit() else ""
             for i in re.split("\D", c)]))
                  if not c.isdigit() else chr(int(c)-1+ord('A'))
                  for c in word.split("-")])
          for word in code.split(" ")])

def allsplit(s, i = 0):
  if len(s) == i:
    return [[s]]
  elif s[i] == " ":
           # Part A                                     # Part B
    return [[s[0:i]] + acc for acc in allsplit(s[i + 1:])] + allsplit(s, i + 1)
  else:
    return allsplit(s, i + 1)


def checkA1z26(result,Input,Output,indice):
     ##A1Z26
       a1lst =[]
       a1lstword =[]

       for word in result.split(" "):
              try:
                    int(word)
                    allnbr = 1
              except:
                    allnbr = 0
 
              if len(word) < 18 and allnbr == 1:
                word = " ".join(word)
                #word = "1 9 1 1 2 2 1 2 0"
                final = []
                joined = []
                res = []
                res = allsplit(word)

                for tojoin in res:
                     tojoin = "".join(tojoin)
                     tojoin = tojoin.replace(" ","-")
                     joined.append(tojoin)
                for postfin in joined:
                     postmp = ""
                     for chunk in postfin.split("-"):
                         cnt = 0
                         for j in chunk:
                                   if cnt >=2:
                                         postmp += "-"
                                         cnt = 0
                                   postmp += j
                                   cnt = cnt +1
                         postmp += "-" 
                     if postmp[-1:] == "-":
                          postmp= postmp[:-1]
                     good2go = 1
                     addone = 0
                     for finalcheck in postmp.split("-"):
                          if int(finalcheck) == 0:
                               addone = 1
                     if addone == 1:
                          newval = []
                          for nbr in postmp.split("-"):
                               plus1 = int(nbr) + 1
                               newval.append(str(plus1))
                          postmp = "-".join(newval)

                     for finalcheck in postmp.split("-"):
                          if int(finalcheck) > 26:
                               good2go = 0
                     if not postmp in final and good2go == 1:
                          FINALW.append(postmp)

                for toa1z26 in final:
                     #print("\n",toa1z26)     
                     wordnbr = A1Z26Cipher(toa1z26)
#                     print(wordnbr)
                     if wordnbr.lower() in wordlist:
                           if not wordnbr.lower() in a1lstword:                        
                              a1lstword.append(wordnbr)
                              a1lst.append(toa1z26.replace("-",""))
                           print("\n==A1Z26==")
                           print("\nFound : ",wordnbr)
                           print("\nA1Z26 : ",toa1z26)
                           if len(a1lstword) >1:
                              mxl = len(max(a1lstword, key=len))
                              print("\nFounds : ",a1lst)
                              print("\nFounds : ",a1lstword)
                              print("Max Word Lenght : ",mxl)
                           print("\nFrom Base %i to Base %i :" % (Input,Output))
                           print("Ic = ",indice)
                #           print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
                           print(result.upper())
                           print("\n==")
                           #try:

                                #if mxl > 3:
                                #     time.sleep(mxl)
                                #else:
                                #     time.sleep(2)
                                #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                                #if mxl >= 5:
                                #   ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
                           #except:
                           #   pass



ic = lambda text: sum(((text.count(l) * (text.count(l) - 1)) / float(len(text) * (len(text) - 1))) for l in text)

base62 = ['0','1','2','3','4','5','6','7','8','9',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#base36 = ['0','1','2','3','4','5','6','7','8','9',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#base26 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

FINALW = []
FINALN = []
FINALB = []
FINALP = []


print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
print("""Description :
Le message suivant a été chiffré par une méthode permettant d'encoder n'importe quel mot, formé uniquement par les 26 lettres de l'alphabet de base (Les "é" sont par exemple remplacés par des "e"), il n'y a donc pas 36 solutions.

Épreuve :
1397803 14'48195211 1670240 19395 62631077351, 20094108 46208 1257644 811'1251 42247273127 697952 43616 55359776 855 1323046484084: 815760084 (1749691977), 23165947 (1739557041), 76056772393675 (36242), 75711293253960356 (1115), 2980227895822964 (1283 34933628), 1378532 75386251628048 (783518-791819), 14'2248595809466. 1242 40131, 694613 1576835 ^^, 1250228 1175 958628 645756845519193808667321647775477622218 58648355260718 :).

2721490350303578 1397803 47587423 1211 1390052, 73252461756371 43616 26799 1257644 56766080 15148 1198498 888313916. 40131 20094400, 7439492854897463082630063250 ;) """)
print("")

crypt = """1397803 14 48195211 1670240 19395 62631077351 20094108 46208 1257644 811 1251 42247273127 697952 43616 55359776 855 1323046484084 815760084 1749691977 23165947 1739557041 76056772393675 36242 75711293253960356 1115 2980227895822964 1283 34933628 1378532 75386251628048 783518 791819 14 2248595809466 1242 40131 694613 1576835 1250228 1175 958628 645756845519193808667321647775477622218 58648355260718 2721490350303578 1397803 47587423 1211 1390052 73252461756371 43616 26799 1257644 56766080 15148 1198498 888313916 40131 20094400 7439492854897463082630063250"""

crypt = crypt.split(" ") 
##todo##
##base to ascii##
##if fail test all nbr one by one##


InputBase = 10
OutputBase = 25

while OutputBase < 122:
  InputBase = 10
  while InputBase < 122:#and InputBase != OutputBase:#OutputBase:

     result = ""

     basemodif = []
     basemodif2 = []

     wordtmpbasea1 = []
     wordtmpbasea0 = []
     wordtmpbasea12 = []
     wordtmpbasea02 = []
     wordtmpbasea13 = []
     wordtmpbasea03 = []

     tmpbasea1 = ""
     tmpbasea0 = ""
     tmpbasea12 = ""
     tmpbasea02 = ""
     tmpbasea13 = ""
     tmpbasea03 = ""


     for nbr in crypt:
          result += base(nbr,InputBase,OutputBase,string = True)
          result += " "

     if InputBase <= 62 and OutputBase <= 62 and OutputBase >= 10 and InputBase >= 10:

             i = 0
             j = 0
             while i <= InputBase:
                  try:
                       basemodif.append(base62[j])
                  except:
                       j = 0
                       basemodif.append(base62[j])
                  i = i + 1
                  j = j + 1

             i = 0
             j = 0
             while i <= OutputBase:
                  try:
                       basemodif2.append(base62[j])
                  except:
                       j = 0
                       basemodif2.append(base62[j])
                  i = i + 1
                  j = j + 1


             for nbr in crypt:
                    tmpbasea1 += baseXtoY(nbr,basemodif,basemodif2)
                    tmpbasea1 += " "
                   
                    tmpbasea0 += baseXtoY2(nbr,basemodif,basemodif2)
                    tmpbasea0 += " "

                    tmpbasea12 += baseXtoY(nbr,basemodif,basemodif2[::-1])
                    tmpbasea12 += " "

                    tmpbasea02 += baseXtoY2(nbr,basemodif,basemodif2[::-1])
                    tmpbasea02 += " "

                    tmpbasea13 += baseXtoY(nbr,basemodif,basemodif[::-1])
                    tmpbasea13 += " "

                    tmpbasea03 += baseXtoY2(nbr,basemodif,basemodif[::-1])
                    tmpbasea03 += " "





     ICres =ic(result)

     if len(tmpbasea0) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea0:
            wordtmpbasea0.append(word.lower())
        try:
          mxl = len(max(wordtmpbasea0, key=len))
        except:
             mxl = 0
        if len(wordtmpbasea0) > 0 :
               print("\n==BASE MODIF A0==")
        #       print("\nFound : ",word)
               print("Founds : ",wordtmpbasea0)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base : ",len(basemodif))
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif2))
               print("Base Alphabet:\n",basemodif2)
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea0.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl >4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in tmpbasea0.split(" "):
                   for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea0 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea0)
               if mxl >= 5:
                             if not tmpbasea0 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea0)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea0,InputBase,OutputBase,ICres)

     if len(tmpbasea1) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea1:
            wordtmpbasea1.append(word.lower())
     try:
             mxl = len(max(wordtmpbasea1, key=len))
     except:
             mxl = 0
     if len(wordtmpbasea1) > 0 :
               print("\n==BASE MODIF A1==")
        #       print("\nFound : ",word)
               print("Founds : ",wordtmpbasea1)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base : ",len(basemodif))
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif2))
               print("Base Alphabet:\n",basemodif2)
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea1.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in tmpbasea1.split(" "):
                    for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea1 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea1)

               if mxl >= 5:
                            if not tmpbasea1 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea1)

               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea1,InputBase,OutputBase,ICres)


     if len(tmpbasea02) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea02:
            wordtmpbasea02.append(word.lower())
     try:
          mxl = len(max(wordtmpbasea02, key=len))
     except:
             mxl = 0
     if len(wordtmpbasea02) > 0 :
               print("\n==BASE MODIF A0==")
              # print("\nFound : ",word)
               print("Founds : ",wordtmpbasea02)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base : ",len(basemodif))
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif2))
               print("Base Alphabet:\n",basemodif2[::-1])
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea02.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in tmpbasea02.split(" "):
                    for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea02 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea02)

               if mxl >= 5:
                             if not tmpbasea02 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea02)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea02,InputBase,OutputBase,ICres)

     if len(tmpbasea12) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea12:
            wordtmpbasea12.append(word.lower())
     try:
          mxl = len(max(wordtmpbasea12, key=len))
     except:
             mxl = 0
     if len(wordtmpbasea12) > 0 :
               print("\n==BASE MODIF A1==")
               #print("\nFound : ",word)
               print("Founds : ",wordtmpbasea12)
               print("\nFrom Base : ",len(basemodif))
               print("Max Word Lenght : ",mxl)
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif2))
               print("Base Alphabet:\n",basemodif2[::-1])
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea12.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)

               for dblcheck in tmpbasea12.split(" "):
                     for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea12 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea12)

               if mxl >= 5:
                             if not tmpbasea12 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea12)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea12,InputBase,OutputBase,ICres)

     if len(tmpbasea03) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea03:
            wordtmpbasea03.append(word.lower())
     try:
             mxl = len(max(wordtmpbasea03, key=len))
     except:
             mxl = 0
     if len(wordtmpbasea03) > 0 :
               print("\n==BASE MODIF A0==")
               #print("\nFound : ",word)
               print("Founds : ",wordtmpbasea03)
               print("\nFrom Base : ",len(basemodif))
               print("Max Word Lenght : ",mxl)
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif))
               print("Base Alphabet:\n",basemodif[::-1])
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea03.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)

               for dblcheck in tmpbasea03.split(" "):
                   for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea03:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea03)

               if mxl >= 5:
                             if not tmpbasea03:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA0")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea03)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea03,InputBase,OutputBase,ICres)

     if len(tmpbasea13) > 0:
        for word in wordlist:
          if word.lower() in tmpbasea13:
            wordtmpbasea13.append(word.lower())
     try:
             mxl = len(max(wordtmpbasea13, key=len))
     except:
             mxl = 0
     if len(wordtmpbasea13) > 0 :
               print("\n==BASE MODIF A1==")
        #       print("\nFound : ",word)
               print("Founds : ",wordtmpbasea13)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base : ",len(basemodif))
               print("Base Alphabet:\n",basemodif)
               print("To Base: ",len(basemodif))
               print("Base Alphabet:\n",basemodif[::-1])
               print("\nIc = ",ICres)
               #print("Reminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(tmpbasea13.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in tmpbasea13.split(" "):
                    for word in wordlist: 
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not tmpbasea13 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea13)

               if mxl >= 5:
                             if not tmpbasea13 in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASEModifA1")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(tmpbasea13)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(tmpbasea13,InputBase,OutputBase,ICres)

     if ICres >= 7 and ICres <= 8:

               print("\n==IC==")
               #print("\nFound : ",word)
               print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
               print("Ic = ",ICres)
               #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16.  Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(result.upper())
               print("\n==")
               #checkA1z26(result,InputBase,OutputBase,ICres)
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #pass #time.sleep(1)
     else:


     ##
       leetres = []
       leetresword = []
       leetres2 = []
       leetresword2 = []


       baseres = []

       for word in wordlist:

          if word.lower() in result.lower():
     #if 1 == 1:
               if not word.lower() in baseres:
                    baseres.append(word.lower())
       try:
               mxl = len(max(baseres, key=len))
       except:
             mxl = 0
       if len(baseres) > 0:
                    print("\n==BASE==")
                    #print("\nFound : ",word)
                    print("\nFounds : ",baseres)
                    print("Max Word Lenght : ",mxl)
                    print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
                    print("Ic = ",ICres)
                    #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
                    print(result.upper())
                    print("\n==")
                    #if mxl > 4:
                    #    time.sleep(mxl)
                    #else:
                    #    pass #time.sleep(1)
                    for dblcheck in result.split(" "):
                       for word in wordlist:
                         if word.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASE")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)

                    if mxl >= 5:
                             if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("BASE")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)

                    #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
                    #checkA1z26(result,InputBase,OutputBase,ICres)

       leetmodif = [tmpbasea1,tmpbasea0,tmpbasea12,tmpbasea02,tmpbasea13,tmpbasea03]

       for modifres in leetmodif:

          leetresmodif = []
          leetreswordmodif = []
          leetresmodif2 = []
          leetreswordmodif2 = []

          for word in wordlist:
               l33t = leet(word)
               l33t2 = leet2(word)
               if len(modifres) > 0:
                    if l33t.lower() in modifres.lower():
                      if not l33t.lower() in leetresmodif:
                         leetresmodif.append( l33t.lower() )
                         leetreswordmodif.append(word)
                    if l33t2.lower() in modifres.lower():
                      if not l33t2.lower() in leetresmodif2:
                         leetresmodif2.append( l33t2.lower() )
                         leetreswordmodif2.append(word)

          if len(leetresmodif) > 0:
                           mxl = len(max(leetresmodif, key=len))
                           print("\n==L33TMODIF==")
                           #print("\nFound %s in leet : %s "%(word,l33t))
                           print("\nList l33t : ",leetresmodif)
                           print("\nList l33t : ",leetreswordmodif)
                           print("Max Word Lenght : ",mxl)
                           print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
                           print("Ic = ",ICres)
                           #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
                           print(modifres.upper())
                           print("\n==")
                           #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                           #if mxl > 4:
                           #     time.sleep(mxl)
                           #else:
                           #     pass #time.sleep(1)
                           for dblcheck in modifres.split(" "):
                                for word in wordlist:
                                     if l33t.upper() == dblcheck.upper():
                                         print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                                         if not modifres in FINALP:
                                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                                 FINALN.append("LEETModif")
                                                 FINALW.append(word)
                                                 FINALB.append(b2b)
                                                 FINALP.append(modifres)

                           if mxl >= 5:
                                         if not modifres in FINALP:
                                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                                 FINALN.append("LEETModif")
                                                 FINALW.append(word)
                                                 FINALB.append(b2b)
                                                 FINALP.append(modifres)
                           #      ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
                           #checkA1z26(modifres,InputBase,OutputBase,ICres)

          if len(leetresmodif2) > 0:
                           mxl = len(max(leetresmodif2, key=len))
                           print("\n==L33T2MODIF==")
                      #     print("\nFound %s in leet : %s "%(word,l33t2))
                           print("\nList l33t2 : ",leetresmodif2)
                           print("\nList l33t2 : ",leetreswordmodif2)
                           print("Max Word Lenght : ",mxl)
                           print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
                           print("Ic = ",ICres)
                           #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16$
                           print(modifres.upper())
                           print("\n==")
                           #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                           #if mxl > 4:
                           #     time.sleep(mxl)
                           #else:
                           #     pass #time.sleep(1)
                           for dblcheck in modifres.split(" "):
                               for word in wordlist:
                                     if l33t2.lower() == dblcheck.lower():
                                         print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                                         if not modifres in FINALP:
                                             b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                             FINALN.append("LEET2Modif")
                                             FINALW.append(word)
                                             FINALB.append(b2b)
                                             FINALP.append(modifres)

                           if mxl >= 5:
                                         if not modifres in FINALP:
                                             b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                             FINALN.append("LEET2Modif")
                                             FINALW.append(word)
                                             FINALB.append(b2b)
                                             FINALP.append(modifres)

                           #        ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
                           #checkA1z26(modifres,InputBase,OutputBase,ICres)

       for word in wordlist:

          l33t = leet(word)

          if l33t.lower() in result.lower():
            if not l33t.lower() in leetres:
                 leetres.append( l33t.lower() )
                 leetresword.append(word)

          l33t2 = leet2(word)

          if l33t2.lower() in result.lower():
            if not l33t2.lower() in leetres2:
                 leetres2.append( l33t2.lower() )
                 leetresword2.append(word)

       if len(leetres) > 0:
               mxl = len(max(leetres, key=len))
               print("\n==L33T==")
               #print("\nFound %s in leet : %s "%(word,l33t))
               print("\nList l33t : ",leetres)
               print("\nList l33t : ",leetresword)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
               print("Ic = ",ICres)
               #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26\n")
               print(result.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in result.split(" "):
                    for word in wordlist:
                         if l33t.upper() == dblcheck.upper():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("LEET")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)

               if mxl >= 5:
                             if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("LEET")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(result,InputBase,OutputBase,ICres)

       if len(leetres2) > 0:
               mxl = len(max(leetres2, key=len))
               print("\n==L33T2==")
          #     print("\nFound %s in leet : %s "%(word,l33t2))
               print("\nList l33t2 : ",leetres2)
               print("\nList l33t2 : ",leetresword2)
               print("Max Word Lenght : ",mxl)
               print("\nFrom Base %i to Base %i :" % (InputBase,OutputBase))
               print("Ic = ",ICres)
               #print("\nReminder :A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16$
               print(result.upper())
               print("\n==")
               #ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
               #if mxl > 4:
               #     time.sleep(mxl)
               #else:
               #     pass #time.sleep(1)
               for dblcheck in result.split(" "):
                   for word in wordlist:
                         if l33t2.lower() == dblcheck.lower():
                             print("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)#ok = input("Exact Match Found ! : %s (Press Enter To Continue ..)\n"%word)
                             if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("LEET2")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)

               if mxl >= 5:
                            if not result in FINALP:
                                 b2b = "From Base %i to %i"%(InputBase,OutputBase)
                                 FINALN.append("LEET2")
                                 FINALW.append(word)
                                 FINALB.append(b2b)
                                 FINALP.append(result)
               #     ok = input("Found len(Word) >= 6 !(Press Enter To Continue ..)\n")
               #checkA1z26(result,InputBase,OutputBase,ICres)

     InputBase = InputBase + 1
  
  OutputBase = OutputBase +1


print("\n\n\n\n")
print("===================================================")
print("===================================================")
print("======================RESULTS======================")
print("===================================================")
print("===================================================\n")


for name,word,baze,plain in zip(FINALN,FINALW,FINALB,FINALP):

     print("\n======")
     print("In Module : ",name)
     print("Found this word : ",word)
     print(baze)
     print("Plain :")
     print(plain)
     print("======\n")

print("So long and thnks for all the fish .\n")
