gText_PkmnTransferredSomeonesPC::
    .string "{STR_VAR_2} a été transféré sur le\n"
    .string "PC de ???.\p"
    .string "Il a été placé dans la Boîte\n"
    .string "appelée “{STR_VAR_1}”.$"

gText_PkmnTransferredLanettesPC::
	.string "{STR_VAR_2} a été transféré sur le\n"
#if IS_FRLG || IS_HNS
	.string "PC de Léo.\p"
#else
	.string "PC de Lanette.\p"
#endif
	.string "Il a été placé dans la Boîte\n"
	.string "appelée “{STR_VAR_1}”.$"

gText_PkmnTransferredSomeonesPCBoxFull::
    .string "La Boîte {STR_VAR_3} sur le PC\n"
    .string "de ??? est pleine.\p"
    .string "{STR_VAR_2} a été placé dans la\n"
    .string "Boîte appelée “{STR_VAR_1}”.$"

gText_PkmnTransferredLanettesPCBoxFull::
	.string "La Boîte “{STR_VAR_3}” sur le\n"
#if IS_FRLG || IS_HNS
	.string "PC de Léo est pleine.\p"
#else
	.string "PC de Lanette est pleine.\p"
#endif
	.string "{STR_VAR_2} a été placé dans la\n"
	.string "Boîte appelée “{STR_VAR_1}”.$"

gText_PkmnSentToPCAfterCatch::
    .string "{STR_VAR_2} a été transféré sur le\n"
	.string "PC de {B_PC_CREATOR_NAME}.\p"
    .string "Il a été placé dans la Boîte\n"
    .string "appelée “{STR_VAR_1}”.$"

gText_PlayerObtainedTheMon::
	.string "{PLAYER} obtained\n"
	.string "the {STR_VAR_1}!$"

gText_NoMoreRoomForPokemon::
    .string "Il n’y a plus de place pour\n"
    .string "les Pokémon.\p"
    .string "Les Boites sont pleines et\n"
    .string "ne peuvent plus rien recevoir.$"

gText_NicknameThisPokemon::
    .string "Voulez-vous donner un surnom\n"
    .string "à {STR_VAR_1}?$"
