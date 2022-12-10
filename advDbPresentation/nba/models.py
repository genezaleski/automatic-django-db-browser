from django.db import models


class Draft(models.Model):
	yearDraft = models.FloatField()
	numberPickOverall = models.FloatField()
	numberRound = models.FloatField()
	numberRoundPick = models.FloatField()
	namePlayer = models.CharField(max_length=50)
	slugTeam = models.CharField(max_length=50)
	nameOrganizationFrom = models.CharField(max_length=50)
	typeOrganizationFrom = models.CharField(max_length=50)
	idPlayer = models.FloatField()
	idTeam = models.FloatField()
	nameTeam = models.CharField(max_length=50)
	cityTeam = models.CharField(max_length=50)
	teamName = models.CharField(max_length=50)
	PLAYER_PROFILE_FLAG = models.FloatField()
	slugOrganizationTypeFrom = models.CharField(max_length=50)
	locationOrganizationFrom = models.CharField(max_length=50)

	class Meta:
		db_table = 'Draft'

	def __str__(self):
		return self.name

class Draft_Combine(models.Model):
	yearCombine = models.IntegerField()
	idPlayer = models.FloatField()
	nameFirst = models.CharField(max_length=50)
	nameLast = models.CharField(max_length=50)
	namePlayer = models.CharField(max_length=50)
	slugPosition = models.CharField(max_length=50)
	heightWOShoesInches = models.FloatField()
	heightWOShoes = models.CharField(max_length=50)
	weightLBS = models.FloatField()
	wingspanInches = models.FloatField()
	wingspan = models.CharField(max_length=50)
	reachStandingInches = models.FloatField()
	reachStandingO = models.CharField(max_length=50)
	verticalLeapStandingInches = models.FloatField()
	verticalLeapMaxInches = models.FloatField()
	timeLaneAgility = models.FloatField()
	timeThreeQuarterCourtSprint = models.FloatField()
	repsBenchPress135 = models.FloatField()
	pctBodyFat = models.FloatField()
	heightWShoesInches = models.FloatField()
	heightWShoes = models.CharField(max_length=50)
	lengthHandInches = models.FloatField()
	widthHandInches = models.FloatField()
	timeModifiedLaneAgility = models.FloatField()
	setSpot15CornerLeft = models.CharField(max_length=50)
	setSpot15BreakLeft = models.CharField(max_length=50)
	setSpot15TopKey = models.CharField(max_length=50)
	setSpot15BreakRight = models.CharField(max_length=50)
	setSpot15CornerRight = models.CharField(max_length=50)
	setSpot15CornerLeftCollege = models.CharField(max_length=50)
	setSpot15BreakLeftCollege = models.CharField(max_length=50)
	setSpot15TopKeyCollege = models.CharField(max_length=50)
	setSpot15BreakRightCollege = models.CharField(max_length=50)
	setSpot15CornerRightCollege = models.CharField(max_length=50)
	setSpot15CornerLeftNBA = models.CharField(max_length=50)
	setSpot15BreakLeftNBA = models.CharField(max_length=50)
	setSpot15TopKeyNBA = models.CharField(max_length=50)
	setSpotBreakRightNBA = models.CharField(max_length=50)
	setSpotCornerRightNBA = models.CharField(max_length=50)
	setSpot15CornerLeftMade = models.FloatField()
	setSpot15CornerLeftAttempted = models.FloatField()
	setSpot15CornerLeftPct = models.FloatField()
	setSpot15BreakLeftMade = models.FloatField()
	setSpot15BreakLeftAttempted = models.FloatField()
	setSpot15BreakLeftPct = models.FloatField()
	setSpot15TopKeyMade = models.FloatField()
	setSpot15TopKeyAttempted = models.FloatField()
	setSpot15TopKeyPct = models.FloatField()
	setSpot15BreakRightMade = models.FloatField()
	setSpot15BreakRightAttempted = models.FloatField()
	setSpot15BreakRightPct = models.FloatField()
	setSpot15CornerRightMade = models.FloatField()
	setSpot15CornerRightAttempted = models.FloatField()
	setSpot15CornerRightPct = models.FloatField()
	setSpot15CornerLeftCollegeMade = models.FloatField()
	setSpot15CornerLeftCollegeAttempted = models.FloatField()
	setSpot15CornerLeftCollegePct = models.FloatField()
	setSpot15BreakLeftCollegeMade = models.FloatField()
	setSpot15BreakLeftCollegeAttempted = models.FloatField()
	setSpot15BreakLeftCollegePct = models.FloatField()
	setSpot15TopKeyCollegeMade = models.FloatField()
	setSpot15TopKeyCollegeAttempted = models.FloatField()
	setSpot15TopKeyCollegePct = models.FloatField()
	setSpot15BreakRightCollegeMade = models.FloatField()
	setSpot15BreakRightCollegeAttempted = models.FloatField()
	setSpot15BreakRightCollegePct = models.FloatField()
	setSpot15CornerRightCollegeMade = models.FloatField()
	setSpot15CornerRightCollegeAttempted = models.FloatField()
	setSpot15CornerRightCollegePct = models.FloatField()
	setSpot15CornerLeftNBAMade = models.FloatField()
	setSpot15CornerLeftNBAAttempted = models.FloatField()
	setSpot15CornerLeftNBAPct = models.FloatField()
	setSpot15BreakLeftNBAMade = models.FloatField()
	setSpot15BreakLeftNBAAttempted = models.FloatField()
	setSpot15BreakLeftNBAPct = models.FloatField()
	setSpot15TopKeyNBAMade = models.FloatField()
	setSpot15TopKeyNBAAttempted = models.FloatField()
	setSpot15TopKeyNBAPct = models.FloatField()
	setSpotBreakRightNBAMade = models.FloatField()
	setSpotBreakRightNBAAttempted = models.FloatField()
	setSpotBreakRightNBAPct = models.FloatField()
	setSpotCornerRightNBAMade = models.FloatField()
	setSpotCornerRightNBAAttempted = models.FloatField()
	setSpotCornerRightNBAPct = models.FloatField()
	setOffDrib15BreakLeft = models.CharField(max_length=50)
	setSpotOffDrib15TopKey = models.CharField(max_length=50)
	setOffDrib15BreakRight = models.CharField(max_length=50)
	setOnMove15 = models.CharField(max_length=50)
	setOnMoveCollege = models.CharField(max_length=50)
	setOffDrib15BreakLeftMade = models.FloatField()
	setOffDrib15BreakLeftAttempted = models.FloatField()
	setOffDrib15BreakLeftPct = models.FloatField()
	setSpotOffDrib15TopKeyMade = models.FloatField()
	setSpotOffDrib15TopKeyAttempted = models.FloatField()
	setSpotOffDrib15TopKeyPct = models.FloatField()
	setOffDrib15BreakRightMade = models.FloatField()
	setOffDrib15BreakRightAttempted = models.FloatField()
	setOffDrib15BreakRightPct = models.FloatField()
	setOnMove15Made = models.FloatField()
	setOnMove15Attempted = models.FloatField()
	setOnMove15Pct = models.FloatField()
	setOnMoveCollegeMade = models.FloatField()
	setOnMoveCollegeAttempted = models.FloatField()
	setOnMoveCollegePct = models.FloatField()
	setOffDribBreakLeftCollege = models.CharField(max_length=50)
	setOffDribTopKeyCollege = models.CharField(max_length=50)
	setOffDribBreakRightCollege = models.CharField(max_length=50)
	setOffDribBreakLeftCollegeMade = models.FloatField()
	setOffDribBreakLeftCollegeAttempted = models.FloatField()
	setOffDribBreakLeftCollegePct = models.FloatField()
	setOffDribTopKeyCollegeMade = models.FloatField()
	setOffDribTopKeyCollegeAttempted = models.FloatField()
	setOffDribTopKeyCollegePct = models.FloatField()
	setOffDribBreakRightCollegeMade = models.FloatField()
	setOffDribBreakRightCollegeAttempted = models.FloatField()
	setOffDribBreakRightCollegePct = models.FloatField()

	class Meta:
		db_table = 'Draft_Combine'

	def __str__(self):
		return self.name

class Game(models.Model):
	GAME_ID = models.CharField(max_length=50)
	SEASON_ID = models.CharField(max_length=50)
	TEAM_ID_HOME = models.CharField(max_length=50)
	TEAM_ABBREVIATION_HOME = models.CharField(max_length=50)
	TEAM_NAME_HOME = models.CharField(max_length=50)
	GAME_DATE = models.CharField(max_length=50)
	MATCHUP_HOME = models.CharField(max_length=50)
	WL_HOME = models.CharField(max_length=50)
	MIN_HOME = models.IntegerField()
	FGM_HOME = models.FloatField()
	FGA_HOME = models.CharField(max_length=50)
	FG_PCT_HOME = models.FloatField()
	FG3M_HOME = models.CharField(max_length=50)
	FG3A_HOME = models.CharField(max_length=50)
	FG3_PCT_HOME = models.FloatField()
	FTM_HOME = models.FloatField()
	FTA_HOME = models.FloatField()
	FT_PCT_HOME = models.FloatField()
	OREB_HOME = models.CharField(max_length=50)
	DREB_HOME = models.CharField(max_length=50)
	REB_HOME = models.CharField(max_length=50)
	AST_HOME = models.CharField(max_length=50)
	STL_HOME = models.CharField(max_length=50)
	BLK_HOME = models.CharField(max_length=50)
	TOV_HOME = models.CharField(max_length=50)
	PF_HOME = models.FloatField()
	PTS_HOME = models.IntegerField()
	PLUS_MINUS_HOME = models.IntegerField()
	VIDEO_AVAILABLE_HOME = models.IntegerField()
	TEAM_ID_AWAY = models.CharField(max_length=50)
	TEAM_ABBREVIATION_AWAY = models.CharField(max_length=50)
	TEAM_NAME_AWAY = models.CharField(max_length=50)
	MATCHUP_AWAY = models.CharField(max_length=50)
	WL_AWAY = models.CharField(max_length=50)
	MIN_AWAY = models.IntegerField()
	FGM_AWAY = models.FloatField()
	FGA_AWAY = models.CharField(max_length=50)
	FG_PCT_AWAY = models.FloatField()
	FG3M_AWAY = models.CharField(max_length=50)
	FG3A_AWAY = models.CharField(max_length=50)
	FG3_PCT_AWAY = models.FloatField()
	FTM_AWAY = models.FloatField()
	FTA_AWAY = models.FloatField()
	FT_PCT_AWAY = models.FloatField()
	OREB_AWAY = models.CharField(max_length=50)
	DREB_AWAY = models.CharField(max_length=50)
	REB_AWAY = models.CharField(max_length=50)
	AST_AWAY = models.CharField(max_length=50)
	STL_AWAY = models.CharField(max_length=50)
	BLK_AWAY = models.CharField(max_length=50)
	TOV_AWAY = models.CharField(max_length=50)
	PF_AWAY = models.FloatField()
	PTS_AWAY = models.IntegerField()
	PLUS_MINUS_AWAY = models.IntegerField()
	VIDEO_AVAILABLE_AWAY = models.IntegerField()
	GAME_DATE_EST = models.CharField(max_length=50)
	GAME_SEQUENCE = models.CharField(max_length=50)
	GAME_STATUS_ID = models.CharField(max_length=50)
	GAME_STATUS_TEXT = models.CharField(max_length=50)
	GAMECODE = models.CharField(max_length=50)
	HOME_TEAM_ID = models.CharField(max_length=50)
	VISITOR_TEAM_ID = models.CharField(max_length=50)
	SEASON = models.CharField(max_length=50)
	LIVE_PERIOD = models.FloatField()
	LIVE_PC_TIME = models.CharField(max_length=50)
	NATL_TV_BROADCASTER_ABBREVIATION = models.CharField(max_length=50)
	LIVE_PERIOD_TIME_BCAST = models.CharField(max_length=50)
	WH_STATUS = models.FloatField()
	TEAM_CITY_HOME = models.CharField(max_length=50)
	PTS_PAINT_HOME = models.CharField(max_length=50)
	PTS_2ND_CHANCE_HOME = models.CharField(max_length=50)
	PTS_FB_HOME = models.CharField(max_length=50)
	LARGEST_LEAD_HOME = models.CharField(max_length=50)
	LEAD_CHANGES_HOME = models.CharField(max_length=50)
	TIMES_TIED_HOME = models.CharField(max_length=50)
	TEAM_TURNOVERS_HOME = models.CharField(max_length=50)
	TOTAL_TURNOVERS_HOME = models.CharField(max_length=50)
	TEAM_REBOUNDS_HOME = models.CharField(max_length=50)
	PTS_OFF_TO_HOME = models.CharField(max_length=50)
	TEAM_CITY_AWAY = models.CharField(max_length=50)
	PTS_PAINT_AWAY = models.CharField(max_length=50)
	PTS_2ND_CHANCE_AWAY = models.CharField(max_length=50)
	PTS_FB_AWAY = models.CharField(max_length=50)
	LARGEST_LEAD_AWAY = models.CharField(max_length=50)
	LEAD_CHANGES_AWAY = models.CharField(max_length=50)
	TIMES_TIED_AWAY = models.CharField(max_length=50)
	TEAM_TURNOVERS_AWAY = models.CharField(max_length=50)
	TOTAL_TURNOVERS_AWAY = models.CharField(max_length=50)
	TEAM_REBOUNDS_AWAY = models.CharField(max_length=50)
	PTS_OFF_TO_AWAY = models.CharField(max_length=50)
	LEAGUE_ID = models.CharField(max_length=50)
	GAME_DATE_DAY = models.CharField(max_length=50)
	ATTENDANCE = models.CharField(max_length=50)
	GAME_TIME = models.CharField(max_length=50)
	TEAM_CITY_NAME_HOME = models.CharField(max_length=50)
	TEAM_NICKNAME_HOME = models.CharField(max_length=50)
	TEAM_WINS_LOSSES_HOME = models.CharField(max_length=50)
	PTS_QTR1_HOME = models.CharField(max_length=50)
	PTS_QTR2_HOME = models.CharField(max_length=50)
	PTS_QTR3_HOME = models.CharField(max_length=50)
	PTS_QTR4_HOME = models.CharField(max_length=50)
	PTS_OT1_HOME = models.CharField(max_length=50)
	PTS_OT2_HOME = models.CharField(max_length=50)
	PTS_OT3_HOME = models.CharField(max_length=50)
	PTS_OT4_HOME = models.CharField(max_length=50)
	PTS_OT5_HOME = models.CharField(max_length=50)
	PTS_OT6_HOME = models.CharField(max_length=50)
	PTS_OT7_HOME = models.CharField(max_length=50)
	PTS_OT8_HOME = models.CharField(max_length=50)
	PTS_OT9_HOME = models.CharField(max_length=50)
	PTS_OT10_HOME = models.CharField(max_length=50)
	PTS_HOME_y = models.FloatField()
	TEAM_CITY_NAME_AWAY = models.CharField(max_length=50)
	TEAM_NICKNAME_AWAY = models.CharField(max_length=50)
	TEAM_WINS_LOSSES_AWAY = models.CharField(max_length=50)
	PTS_QTR1_AWAY = models.CharField(max_length=50)
	PTS_QTR2_AWAY = models.CharField(max_length=50)
	PTS_QTR3_AWAY = models.CharField(max_length=50)
	PTS_QTR4_AWAY = models.CharField(max_length=50)
	PTS_OT1_AWAY = models.CharField(max_length=50)
	PTS_OT2_AWAY = models.CharField(max_length=50)
	PTS_OT3_AWAY = models.CharField(max_length=50)
	PTS_OT4_AWAY = models.CharField(max_length=50)
	PTS_OT5_AWAY = models.CharField(max_length=50)
	PTS_OT6_AWAY = models.CharField(max_length=50)
	PTS_OT7_AWAY = models.CharField(max_length=50)
	PTS_OT8_AWAY = models.CharField(max_length=50)
	PTS_OT9_AWAY = models.CharField(max_length=50)
	PTS_OT10_AWAY = models.CharField(max_length=50)
	LAST_GAME_ID = models.CharField(max_length=50)
	LAST_GAME_DATE_EST = models.CharField(max_length=50)
	LAST_GAME_HOME_TEAM_ID = models.CharField(max_length=50)
	LAST_GAME_HOME_TEAM_CITY = models.CharField(max_length=50)
	LAST_GAME_HOME_TEAM_NAME = models.CharField(max_length=50)
	LAST_GAME_HOME_TEAM_ABBREVIATION = models.CharField(max_length=50)
	LAST_GAME_HOME_TEAM_POINTS = models.CharField(max_length=50)
	LAST_GAME_VISITOR_TEAM_ID = models.CharField(max_length=50)
	LAST_GAME_VISITOR_TEAM_CITY = models.CharField(max_length=50)
	LAST_GAME_VISITOR_TEAM_NAME = models.CharField(max_length=50)
	LAST_GAME_VISITOR_TEAM_CITY1 = models.CharField(max_length=50)
	LAST_GAME_VISITOR_TEAM_POINTS = models.CharField(max_length=50)
	HOME_TEAM_WINS = models.FloatField()
	HOME_TEAM_LOSSES = models.FloatField()
	SERIES_LEADER = models.CharField(max_length=50)
	VIDEO_AVAILABLE_FLAG = models.FloatField()
	PT_AVAILABLE = models.FloatField()
	PT_XYZ_AVAILABLE = models.FloatField()
	HUSTLE_STATUS = models.FloatField()
	HISTORICAL_STATUS = models.FloatField()

	class Meta:
		db_table = 'Game'

	def __str__(self):
		return self.name

class Game_Inactive_Players(models.Model):
	PLAYER_ID = models.CharField(max_length=50)
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	JERSEY_NUM = models.CharField(max_length=50)
	TEAM_ID = models.CharField(max_length=50)
	TEAM_CITY = models.CharField(max_length=50)
	TEAM_NAME = models.CharField(max_length=50)
	TEAM_ABBREVIATION = models.CharField(max_length=50)
	GAME_ID = models.CharField(max_length=50)

	class Meta:
		db_table = 'Game_Inactive_Players'

	def __str__(self):
		return self.name

class Game_Officials(models.Model):
	OFFICIAL_ID = models.CharField(max_length=50)
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	JERSEY_NUM = models.CharField(max_length=50)
	GAME_ID = models.CharField(max_length=50)

	class Meta:
		db_table = 'Game_Officials'

	def __str__(self):
		return self.name

class Player(models.Model):
	id = models.CharField(max_length=50,primary_key=True)
	full_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	is_active = models.IntegerField()

	class Meta:
		db_table = 'Player'

	def __str__(self):
		return self.name

class Player_Attributes(models.Model):
	ID = models.CharField(max_length=50,primary_key=True)
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	DISPLAY_FIRST_LAST = models.CharField(max_length=50)
	DISPLAY_LAST_COMMA_FIRST = models.CharField(max_length=50)
	DISPLAY_FI_LAST = models.CharField(max_length=50)
	PLAYER_SLUG = models.CharField(max_length=50)
	BIRTHDATE = models.CharField(max_length=50)
	SCHOOL = models.CharField(max_length=50)
	COUNTRY = models.CharField(max_length=50)
	LAST_AFFILIATION = models.CharField(max_length=50)
	HEIGHT = models.FloatField()
	WEIGHT = models.FloatField()
	SEASON_EXP = models.IntegerField()
	JERSEY = models.CharField(max_length=50)
	POSITION = models.CharField(max_length=50)
	ROSTERSTATUS = models.CharField(max_length=50)
	GAMES_PLAYED_CURRENT_SEASON_FLAG = models.CharField(max_length=50)
	TEAM_ID = models.CharField(max_length=50)
	TEAM_NAME = models.CharField(max_length=50)
	TEAM_ABBREVIATION = models.CharField(max_length=50)
	TEAM_CODE = models.CharField(max_length=50)
	TEAM_CITY = models.CharField(max_length=50)
	PLAYERCODE = models.CharField(max_length=50)
	FROM_YEAR = models.CharField(max_length=50)
	TO_YEAR = models.CharField(max_length=50)
	DLEAGUE_FLAG = models.CharField(max_length=50)
	NBA_FLAG = models.CharField(max_length=50)
	GAMES_PLAYED_FLAG = models.CharField(max_length=50)
	DRAFT_YEAR = models.CharField(max_length=50)
	DRAFT_ROUND = models.CharField(max_length=50)
	DRAFT_NUMBER = models.CharField(max_length=50)
	PTS = models.FloatField()
	AST = models.FloatField()
	REB = models.FloatField()
	ALL_STAR_APPEARANCES = models.FloatField()
	PIE = models.FloatField()

	class Meta:
		db_table = 'Player_Attributes'

	def __str__(self):
		return self.name

class Player_Bios(models.Model):
	namePlayerBREF = models.CharField(max_length=50)
	urlPlayerBioBREF = models.CharField(max_length=50)
	nameTable = models.CharField(max_length=50)
	urlPlayerImageBREF = models.CharField(max_length=50)
	slugPlayerBREF = models.CharField(max_length=50)
	numberTransactionPlayer = models.IntegerField()
	dateTransaction = models.FloatField()
	descriptionTransaction = models.CharField(max_length=50)
	isGLeagueMovement = models.IntegerField()
	isDraft = models.IntegerField()
	isSigned = models.IntegerField()
	isWaived = models.IntegerField()
	isTraded = models.IntegerField()
	slugSeason = models.CharField(max_length=50)
	nameTeam = models.CharField(max_length=50)
	slugLeague = models.CharField(max_length=50)
	amountSalary = models.FloatField()
	detailsContract = models.CharField(max_length=50)
	namePronunciation = models.CharField(max_length=50)
	namePosition = models.CharField(max_length=50)
	heightInches = models.FloatField()
	weightLBS = models.FloatField()
	dateBirth = models.FloatField()
	locationBirthplace = models.CharField(max_length=50)
	cityBirthplace = models.CharField(max_length=50)
	stateBirthplace = models.CharField(max_length=50)
	nameCollege = models.CharField(max_length=50)
	nameHighSchool = models.CharField(max_length=50)
	dateNBADebut = models.FloatField()
	careerlength = models.CharField(max_length=50)
	yearsExperience = models.FloatField()
	nameTwitter = models.CharField(max_length=50)
	yearHighSchool = models.FloatField()
	rankHighSchool = models.FloatField()
	dateDeath = models.FloatField()
	highschools = models.CharField(max_length=50)
	descriptionRelatives = models.CharField(max_length=50)
	descriptionHOF = models.CharField(max_length=50)
	playerNicknames = models.CharField(max_length=50)
	colleges = models.CharField(max_length=50)

	class Meta:
		db_table = 'Player_Bios'

	def __str__(self):
		return self.name

class Player_Photos(models.Model):
	isActive = models.IntegerField()
	isRookie = models.IntegerField()
	namePlayer = models.CharField(max_length=50)
	idPlayer = models.FloatField()
	countSeasons = models.FloatField()
	yearSeasonFirst = models.FloatField()
	yearSeasonLast = models.FloatField()
	idTeam = models.FloatField()
	hasGamesPlayedFlag = models.IntegerField()
	urlPlayerStats = models.CharField(max_length=50)
	urlPlayerThumbnail = models.CharField(max_length=50)
	urlPlayerHeadshot = models.CharField(max_length=50)
	urlPlayerActionPhoto = models.CharField(max_length=50)
	hasHeadShot = models.IntegerField()
	hasThumbnail = models.IntegerField()
	hasAction = models.IntegerField()
	urlPlayerPhoto = models.CharField(max_length=50)

	class Meta:
		db_table = 'Player_Photos'

	def __str__(self):
		return self.name

class Player_Salary(models.Model):
	slugSeason = models.CharField(max_length=50)
	nameTeam = models.CharField(max_length=50)
	namePlayer = models.CharField(max_length=50)
	statusPlayer = models.CharField(max_length=50)
	isFinalSeason = models.IntegerField()
	isWaived = models.IntegerField()
	isOnRoster = models.IntegerField()
	isNonGuaranteed = models.IntegerField()
	isTeamOption = models.IntegerField()
	isPlayerOption = models.IntegerField()
	typeContractDetail = models.CharField(max_length=50)
	value = models.FloatField()

	class Meta:
		db_table = 'Player_Salary'

	def __str__(self):
		return self.name

class Team(models.Model):
	id = models.CharField(max_length=50,primary_key=True)
	full_name = models.CharField(max_length=50)
	abbreviation = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	year_founded = models.IntegerField()

	class Meta:
		db_table = 'Team'

	def __str__(self):
		return self.name

class Team_Attributes(models.Model):
	ID = models.CharField(max_length=50,primary_key=True)
	ABBREVIATION = models.CharField(max_length=50)
	NICKNAME = models.CharField(max_length=50)
	YEARFOUNDED = models.CharField(max_length=50)
	CITY = models.CharField(max_length=50)
	ARENA = models.CharField(max_length=50)
	ARENACAPACITY = models.FloatField()
	OWNER = models.CharField(max_length=50)
	GENERALMANAGER = models.CharField(max_length=50)
	HEADCOACH = models.CharField(max_length=50)
	DLEAGUEAFFILIATION = models.CharField(max_length=50)
	FACEBOOK_WEBSITE_LINK = models.CharField(max_length=50)
	INSTAGRAM_WEBSITE_LINK = models.CharField(max_length=50)
	TWITTER_WEBSITE_LINK = models.CharField(max_length=50)

	class Meta:
		db_table = 'Team_Attributes'

	def __str__(self):
		return self.name

class Team_History(models.Model):
	ID = models.CharField(max_length=50,primary_key=True)
	CITY = models.CharField(max_length=50)
	NICKNAME = models.CharField(max_length=50)
	YEARFOUNDED = models.CharField(max_length=50)
	YEARACTIVETILL = models.CharField(max_length=50)

	class Meta:
		db_table = 'Team_History'

	def __str__(self):
		return self.name

class Team_Salary(models.Model):
	nameTeam = models.CharField(max_length=50)
	slugTeam = models.CharField(max_length=50)
	urlTeamSalaryHoopsHype = models.CharField(max_length=50)

	class Meta:
		db_table = 'Team_Salary'

	def __str__(self):
		return self.name

