.set LOCALID_MOM, 1
.set LOCALID_MOMS_FRIEND, 2

NewBarkTown_PlayersHouse_1F_hns_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NewBarkTown_PlayersHouse_1F_OnTransition
	.byte 0

NewBarkTown_PlayersHouse_1F_OnTransition::
	call_if_eq VAR_NEWBARK_TOWN_STATE, 1, NewBarkTown_PlayersHouse_1F_SetMomStandingAtTable
	call_if_eq VAR_NEWBARK_TOWN_STATE, 2, NewBarkTown_PlayersHouse_1F_SetMomStandingAtTable
	call_if_eq VAR_NEWBARK_TOWN_STATE, 3, NewBarkTown_PlayersHouse_1F_SetMomStandingAtTable
	end

NewBarkTown_PlayersHouse_1F_SetMomStandingAtTable::
	setobjectxyperm LOCALID_MOM, 8, 4
	setobjectmovementtype LOCALID_MOM, MOVEMENT_TYPE_FACE_LEFT

	@add to newgame later
	clearflag FLAG_HIDE_MOMS_FRIEND
	clearflag FLAG_MOM_VISITED
	return

NewBarkTown_PlayersHouse_1F_EventScript_Mom::
	lock
	faceplayer
	goto_if_set FLAG_MOM_VISITED, NewBarkTown_PlayersHouse_1F_EventScript_Mom_Regular
	goto_if_set FLAG_ADVENTURE_STARTED, NewBarkTown_PlayersHouse_1F_MomEventScript_GoodLuck
	msgbox NewBarkTown_PlayersHouse_1F_Text_MomHurryUpElmIsWaiting, MSGBOX_DEFAULT
	applymovement LOCALID_MOM, NewBarkTown_PlayersHouse_1F_MovementFaceLeft
	waitmovement 0
	release
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomsFriend::
	lock
	faceplayer
	msgbox NewBarkTown_PlayersHouse_1F_Text_MomsFriend, MSGBOX_DEFAULT
	applymovement LOCALID_MOMS_FRIEND, NewBarkTown_PlayersHouse_1F_MovementFaceRight
	waitmovement 0
	release
	end

NewBarkTown_PlayersHouse_1F_MomEventScript_GoodLuck::
	msgbox NewBarkTown_PlayersHouse_1F_Text_MomLeaving, MSGBOX_DEFAULT
	setflag FLAG_MOM_VISITED
	clearflag FLAG_HIDE_ROUTE_30_NPCS
	setvar VAR_NEWBARK_TOWN_STATE, 5
	release
	end


NewBarkTown_PlayersHouse_1F_EventScript_Mom_Regular::
	call NewBarkTown_PlayersHouse_1F_EventScript_MomHealsParty
	release
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomsIntroTrigger1::
	lock
	applymovement LOCALID_PLAYER, NewBarkTown_PlayersHouse_1F_PlayerIntroMovement1
	waitmovement 0
	goto NewBarkTown_PlayersHouse_1F_EventScript_MomsIntro
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomsIntroTrigger2::
	lock
	applymovement LOCALID_PLAYER, NewBarkTown_PlayersHouse_1F_PlayerIntroMovement2
	waitmovement 0
	goto NewBarkTown_PlayersHouse_1F_EventScript_MomsIntro
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomsIntro::
	playse SE_PIN
	applymovement LOCALID_MOM, Common_Movement_ExclamationMark
	delay 60
	applymovement LOCALID_MOM, NewBarkTown_PlayersHouse_1F_MomMovement_1
	waitmovement 0
	msgbox NewBarkTown_PlayersHouse_1F_Text_ElmsLookingForYou, MSGBOX_DEFAULT
	call NewBarkTown_PlayersHouse_1F_EventScript_GivePokeGear
	call NewBarkTown_PlayersHouse_1F_EventScript_GiveRunningShoes
	applymovement LOCALID_MOM, NewBarkTown_PlayersHouse_1F_MomMovement_2
	waitmovement 0
	setvar VAR_NEWBARK_TOWN_STATE, 2
	setvar VAR_NEWBARKTOWN_LABSTATE, 0
	setflag FLAG_HIDE_LAB_POLICEMAN
	setflag FLAG_VISITED_NEWBARK_TOWN

	@former flagheap location

	releaseall
	end

NewBarkTown_PlayersHouse_1F_EventScript_GivePokeGear::
	playfanfare MUS_OBTAIN_ITEM
	message NewBarkTown_PlayersHouse_1F_Text_ObtainedPokeGear
	waitfanfare
	setflag FLAG_SYS_POKENAV_GET
	setflag FLAG_RECEIVED_POKENAV
	setflag FLAG_ADDED_MATCH_CALL_TO_POKENAV
	setflag FLAG_REGISTER_RIVAL_POKENAV
	msgbox NewBarkTown_PlayersHouse_1F_Text_ExplainPokeGear, MSGBOX_DEFAULT
	closemessage
	delay 30
	return
	
NewBarkTown_PlayersHouse_1F_EventScript_GiveRunningShoes::
	msgbox NewBarkTown_PlayersHouse_1F_Text_WearTheseRunningShoes, MSGBOX_DEFAULT
	waitmessage
	closemessage
	playfanfare MUS_OBTAIN_ITEM
	msgbox NewBarkTown_PlayersHouse_1F_Text_SwitchShoesWithRunningShoes, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	setflag FLAG_RECEIVED_RUNNING_SHOES
	setflag FLAG_SYS_B_DASH
	msgbox NewBarkTown_PlayersHouse_1F_Text_ExplainRunningShoes, MSGBOX_DEFAULT
	closemessage
	delay 30
	return

EventScript_RunningShoesManual::
	msgbox NewBarkTown_PlayersHouse_1F_Text_ExplainRunningShoes, MSGBOX_SIGN
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomHealsParty::
	@ specialvar VAR_RESULT, IsPokecenterChallengeActivated
	@ goto_if_eq VAR_RESULT, TRUE, NewBarkTown_PlayersHouse_1F_EventScript_MomHealsParty_PokecenterChallenge
	msgbox NewBarkTown_PlayersHouse_1F_Text_YouShouldRestABit, MSGBOX_DEFAULT
	goto NewBarkTown_PlayersHouse_1F_EventScript_HealParty
	end

NewBarkTown_PlayersHouse_1F_EventScript_HealParty::
	closemessage
	call Common_EventScript_OutOfCenterPartyHeal
	incrementgamestat GAME_STAT_RESTED_AT_HOME
	msgbox NewBarkTown_PlayersHouse_1F_Text_TakeCareHoney, MSGBOX_DEFAULT
	release
	end

NewBarkTown_PlayersHouse_1F_EventScript_MomHealsParty_PokecenterChallenge::
	msgbox NewBarkTown_PlayersHouse_1F_Text_YouShouldRestABit_PokecenterChallenge, MSGBOX_DEFAULT
	closemessage
	end

NewBarkTown_PlayersHouse_1F_Text_YouShouldRestABit_PokecenterChallenge:
	.string "Maman: Désolée mon chérie, tu joues\n"
	.string "avec le challenge du Pokécentre !$"

NewBarkTown_PlayersHouse_1F_Text_YouShouldRestABit:
    .string "Maman: Comment ça va, {PLAYER}?\n"
    .string "Tu as l’air raplapla.\p"
    .string "Tu devrais peut-être te reposer.$"

@ HnS
Common_Text_ReceivedMon:
	.string "{PLAYER} reçoit {STR_VAR_1}!$"

Common_Text_PartyIsFull:
	.string "Wow, attends. Tu ne peux pas\n"
	.string "transporter plus de Pokémon.$"

Common_Text_LookCloserAtMap:
	.string "{PLAYER} regarde attentivement la\n"
	.string "carte de la région.$"

NewBarkTown_PlayersHouse_1F_PlayerIntroMovement1:
	delay_8
	walk_down
	walk_right
	walk_down
	face_left
	delay_8
	step_end

NewBarkTown_PlayersHouse_1F_PlayerIntroMovement2:
	delay_8
	walk_down
	face_left
	delay_8
	step_end

NewBarkTown_PlayersHouse_1F_MomMovement_1:
	face_right
	walk_right
	step_end

NewBarkTown_PlayersHouse_1F_MomMovement_2:
	face_left
	walk_left
	delay_8
	step_end

NewBarkTown_PlayersHouse_1F_MovementFaceRight:
	face_right
	step_end

NewBarkTown_PlayersHouse_1F_MovementFaceLeft:
	face_left
	step_end

NewBarkTown_PlayersHouse_1F_Text_ElmsLookingForYou:
	.string "Ah, {PLAYER}… ! Notre voisin,\n"
	.string "le Prof. Orme, te cherchait.\p"
	.string "Il voulait tu fasses quelque\n"
	.string "chose pour lui.\p"
	.string "Oh ! J'allais oublier !\n"
	.string "Ton Pokématos est revenu de\l"
    .string "chez le réparateur.\p"
	.string "Tiens !$"

NewBarkTown_PlayersHouse_1F_Text_ObtainedPokeGear:
	.string "{PLAYER} reçoit le Pokématos.$"

NewBarkTown_PlayersHouse_1F_Text_ExplainPokeGear:
	.string "MOM: Phone numbers are stored\n"
	.string "in memory.\p"
	.string "Just choose a name you want to call.\p"
	.string "Gee, isn't that convenient?$"

NewBarkTown_PlayersHouse_1F_Text_WearTheseRunningShoes:
	.string "Oh, and don't forget your\n"
	.string "RUNNING SHOES!$"

NewBarkTown_PlayersHouse_1F_Text_SwitchShoesWithRunningShoes:
	.string "{PLAYER} switched shoes with the\n"
	.string "RUNNING SHOES.$"

NewBarkTown_PlayersHouse_1F_Text_ExplainRunningShoes:
	.string "MOM: {PLAYER}, press the B Button\n"
	.string "while wearing these to run fast!$"

NewBarkTown_PlayersHouse_1F_Text_MomHurryUpElmIsWaiting:
	.string "MOM: PROF.ELM is waiting for you.\p"
	.string "Hurry up, baby!$"

NewBarkTown_PlayersHouse_1F_Text_MomsFriend:
	.string "Hi, {PLAYER}!\p"
	.string "I'm visiting!\p"
	.string "Have you heard?\p"
	.string "My daughter is adamant about\n"
	.string "becoming PROF.ELM's assistant.\p"
	.string "She really loves POKéMON!$"

NewBarkTown_PlayersHouse_1F_Text_MomLeaving:
	.string "MOM: Wow, that's a cute POKéMON.\n"
	.string "Where did you get it?\p"
	.string "…\p"
	.string "So, you're leaving on an adventure...\n"
	.string "That does sound challenging...\p"
	.string "Just be careful.\p"
	.string "POKéMON are your friends.\n"
	.string "You need to work as a team.\p"
	.string "Now, go on!\n"
	.string "I'm behind you all the way!$"

NewBarkTown_PlayersHouse_1F_Text_TakeCareHoney:
	.string "MOM: Take care, honey!$"

LilycoveCity_ContestLobby_Text_PleaseDecideLinkLeader:
	.string "Please decide which of you will\n"
	.string "become the GROUP LEADER.\p"
	.string "The other players must then choose\n"
	.string "“JOIN GROUP.”$"

TrainerHill_1F_EventScript_Lost::
	trainerhill_settrainerflags
	trainerhill_lost
	setvar VAR_TEMP_1, 1
	end
