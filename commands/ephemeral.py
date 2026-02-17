import discord

async def my_slash_command(interaction: discord.Interaction):
	await interaction.response.send_message("This is ephemeral!", ephemeral=True)


module = {
	"type": "command",
	"name": "ephemeral",
	"description": "My Ephemeral Response",
	"callback": my_slash_command
}
