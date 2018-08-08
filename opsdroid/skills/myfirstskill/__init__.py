from opsdroid.matchers import match_regex

@match_regex(r"how are you\?")

async def how_are_you(opsdroid, config, message):
	await message.respond("I'm fine thanks!")
