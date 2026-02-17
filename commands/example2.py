import discord

async def my_slash_command(interaction: discord.Interaction):
	await interaction.response.send_message("This is my other example command!!!")


module = {
	"type": "command",
	"name": "example2",
	"description": "My Other Description",
	"callback": my_slash_command
}
