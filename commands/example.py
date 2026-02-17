import discord

async def my_slash_command(interaction: discord.Interaction):
	await interaction.response.send_message("This is my example command!")


module = {
	"type": "command",
	"name": "example",
	"description": "My Description",
	"callback": my_slash_command
}
