<p align="center">
    <img src="https://github.com/Laernos/Husky/assets/55562998/2599079e-6371-4e72-944c-936ab0b532a1.png" alt="Husky Bot Logo" width="500">
</p>

Husky Bot is a Discord bot that is designed to help manage your Discord server. It includes a wide range of features, including moderation tools, utility commands, and fun commands to keep your server engaged.

## Table of Contents
- ✨ [Features](#features)
- 📜 [Commands](#commands)
- 🛠️ [Installation](#installation)
- 🤝 [Contributing](#contributing)
- 🔒 [License](#license)

## Features

<details>
<summary>Responsive Module Management</summary>
<br><table><tr>
<td valign="top">
Turn modules on or off with an intuitive toggle system, giving you complete control over your server's functionality.
</td>
<td align="right">
    <img src="https://github.com/Laernos/Husky/assets/55562998/604c1edb-36b6-4b27-a137-4a51ee89c828.gif" alt="Main Feature" width="600">
</td>
</tr></table></details>

<details>
<summary>Cloud-Based Storage with MongoDB</summary>
<br>
<table>
  <tr>
    <td valign="top">
Husky Bot harnesses the power of MongoDB, to ensure smooth management and operation across multiple servers. Each time Husky joins a new Discord server, it cleverly creates a unique database entry. This means every server gets its own dedicated space for bot configurations and data, allowing for highly personalized settings.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/2057963e-b47c-4454-a389-e9f5ff3ce6e5.png" alt="MongoDB" width="1500">
    </td>
  </tr>
  <tr>
    <td valign="top">
As the owner, you have full control over the bot's interactions with various servers. Whenever the bot joins or leaves a server, it automatically sends a notification to the support server. This notification includes essential information like the server owner's name, the total member count of the server, and the server's icon. This feature is designed to keep you well-informed about the bot's presence across different servers, ensuring effective monitoring and management of its activities.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/0d5af50f-57b7-4d16-a1f1-373911420a6b.png" alt="On server join" width="1500">
    </td>
  </tr>
</table>
</details>

<details>
<summary>Effortlessly Report Users or Messages</summary>
<br><table><tr>
<td valign="top">
The report module is a context menu, it allows members to access additional options by right-clicking on a member or message in the server.

If members right-click on a member, they will see an option to report them. If they select this option, they will be asked to provide a reason for the report.
This report will be sent to the server moderators.

If members right-click on a message, they will see an option to report the message. If they select this option, they will be asked to provide a reason for the report.
This report will be sent to the server moderators.
</td>
<td align="right">
    <img src="https://github.com/Laernos/Husky/assets/55562998/bbae1c39-b468-4278-9204-aa88e3543267.gif" alt="Report Message" width="500">
</td>
</tr></table></details>

<details>
<summary>Efficient Bug Reporting</summary>
<br><table><tr>
<td valign="top">
When server owners encounter issues with Husky Bot, they can easily report these through a user-friendly form directly within Discord.

Once a bug report is submitted, the system automatically sends a copy to both the reporter and the bot's support server. 

Users can report bugs effortlessly, ensuring quick fixes and stable performance.
</td>
<td align="right">
    <img src="https://github.com/Laernos/Husky/assets/55562998/e331d0f3-04fe-4bf6-8a7b-dbbe9f84b240.gif" alt="Bug Report" width="600">
</td>
</tr></table></details>

<details>
<summary>Advanced Logging</summary>
    <h3>Gain insights into your server's activity with detailed logs and analytics.</h3>
<br>
<table>
  <tr>
    <td valign="top">
        Server Logging <br><br>
      Tracks key server-wide events, such as role changes, channel updates, and server settings alterations.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/b2a9009f-22c5-4414-a746-7b76e418246c.png" alt="Toggle System" width="400">
    </td>
    <td valign="top">
        Member Logging <br><br>
      Monitors individual member actions like joins, leaves, nickname changes, and role assignments.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/23d9e403-2ac8-4047-81c1-be45925339b8.png" alt="Server Activity Insights" width="400">
    </td>
  </tr>
  <tr>
    <td valign="top">
        Moderation Logging <br><br>
      Records all moderation actions, such as kicks, bans, and unbans, providing a clear audit trail for moderators' actions.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/772d0209-1a19-4270-9e56-169b15b66cbc.png" alt="Real-time Monitoring" width="2000">
    </td>
    <td valign="top">
        Message Logging <br><br>
      Keeps a record of message activities, including message edits and deletions, which can be crucial for resolving disputes and monitoring compliance with server rules.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/2e9200db-456f-4bac-b6db-b170c1fd10c4.png" alt="Customizable Logging" width="2000">
    </td>
  </tr>
  <tr>
    <td valign="top">
        Voice Logging <br><br>
      Logs all voice channel activities, such as users joining or leaving voice channels, which can be useful for managing voice chat and resolving any related issues.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/f3c62a05-232e-4bef-81f5-1143f49c974c.png" alt="User-friendly Interface" width="800">
    </td>
    <td valign="top">
        Activity Logging <br><br>
      Keeps track of user statuses, such as when members start or stop playing games. This allows moderators to see who is active and what games are popular within the community.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/1df4e974-91a4-4565-86bf-60405566abb1.png" alt="Advanced Security" width="2000">
    </td>
  </tr>
</table>
</details>

<details>
<summary>Welcome Module</summary>
<br><table><tr>
<td valign="top">
The welcome module is a feature that allows you to customize the greeting message that is sent to new members when they join your server.

The bot will send a banner card to the designated channel every time a new member joins the server. The banner card will include the new member's name and profile picture.

The welcome module is a great way to make new members feel welcomed and included in your server. Have fun greeting your new members!
</td>
<td align="right">
    <img src="https://github.com/Laernos/Husky/assets/55562998/ee66798e-502f-468c-8a5d-997337d2b40c.png" alt="Welcome Banner" width="1000">  
</td>
</tr></table></details>

<details>
<summary>Fun Games</summary>
<br>
<table>
  <tr>
    <td valign="top">
      🔢 Counting Numbers<br>
      Welcome to the counting numbers! In this activity, members can participate by counting up in order.<br><br>
      To join the event, simply type a number in the channel. The next person must then type the next number in the sequence, and so on.<br><br>
      Rules:<br>
      - Only numbers are allowed (no decimals or negative numbers).<br>
      - You must type the next number in the sequence (e.g., if the last number typed was 3, you must type 4).<br>
      - Do not type a number that has already been used.<br>
      - Do not spam the channel with numbers.
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/3b5aa61a-d6d2-49e7-a8ea-5804cb4a6bae.png" alt="Count Numbers" width="800">   
    </td>
  </tr>
  <tr>
    <td valign="top">
      💯 Guessing Numbers<br>
      Welcome to guessing the numbers! In this activity, the bot will create a random number between 0 and 100, and users will try to guess the number.<br><br>
      To participate, simply type your guess in the designated channel.<br><br>
      If you try to guess the number 5 times without success, the bot will give you a hint by saying the number is between two specific numbers (e.g., "The number is between 50 and 75").<br><br>
      The first person to guess the correct number wins the event. Have fun guessing!
    </td>
    <td>
      <img src="https://github.com/Laernos/Husky/assets/55562998/c3a87a8f-6b42-4e0c-aa1a-7dd93729d710.png" alt="Guess Number" width="800">    
    </td>
  </tr>
</table>
</details>


## Commands

**General Commands**  
- `avatar`: Displays the user's avatar.  
- `echo`: Repeats the message back to you.  
- `huskies`: Information about huskies.  
- `stats`: Shows the bot's statistics.

**Moderation Commands**  
- `ban`: Bans a user from the server.  
- `unban`: Unbans a user from the server.  
- `kick`: Kicks a user from the server.

**Fun Commands**  
- `rockpaperscissors`: Play Rock, Paper, Scissors with the bot.  
- `guess`: Guess a number game.  
- `slot`: Slot machine game.  
- `roll`: Roll a dice.  
- `dropout_chance`: Calculates the chance of a hypothetical dropout.

**Server Config Commands**  
- `prefix`: Sets or shows the bot's prefix.  
- `welcome`: Configures welcome messages.  
- `logging`: Sets up logging features.

**Owner Commands**  
- `reload`: Reloads a bot's command.  
- `resetdb`: Resets the database of the guild.


## Installation
<details>
<summary>Installation Steps:</summary>
<br>
Follow these steps to install and set up Husky:

1. **Clone the Repository:**

   Open your terminal or command prompt and navigate to the directory where you want to store your bot's code. Then, run the following command to clone the bot's repository:

   ```
   git clone https://github.com/Laernos/Husky.git
   ```
   
2. **Navigate to the Bot's Directory:**
   ```
   cd Husky
   ```

3. **Install Python and Dependencies:**
   
   Ensure you have Python installed on your system. You can download it from Python's official website. Next, create a virtual environment and activate it (recommended for isolation):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```
4. **Invite the Bot to Your Discord Server:**

   - Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/docs/getting-started).

   - Copy your bot's token.

   - Use the provided invite link template or generate an OAuth2 invite link with the "bot" scope and the necessary permissions. Invite the bot to your server.
  

5. **MongoDB SETUP**
   
   Husky uses MongoDB for data storage. If you don't have a MongoDB account, follow these steps to create one:
    Create a MongoDB Atlas Account:
    
    - **Visit MongoDB Atlas:**
       
        Sign up for an account or log in if you already have one.
   
   - **Create a Cluster:**
    
        Once logged in, create a new cluster by following the provided instructions.
        Select a cloud provider and region that best suits your needs.
     
    - **Set Up Database User:**
    
        In your MongoDB Atlas dashboard, navigate to the "Database Access" section.
        Click "Add New Database User" and create a username and password. Remember these credentials.
   
    - **Whitelist Your IP Address:**
    
        In the "Network Access" section, click "Add IP Address" and whitelist your current IP address.
      
    - **Get Connection String:**
    
        In your cluster's dashboard, click "Connect" and choose "Connect Your Application."
      
        Copy the connection string and replace <password> with the database user's password.
      
        Example connection string:
        ```
        mongodb+srv://<username>:<password>@cluster0.mongodb.net/<database-name>?retryWrites=true&w=majority
        ```

      
5. **Configure the bot**
   
    Create a `.env` file in the root directory of your Husky bot project and fill it with the following variables:
   ```env
    DISCORD_API_TOKEN= "YOUR_DISCORD_API_TOKEN_HERE"
    GUILD = "YOUR_GUILD_NAME"
    GUILD_INVITE = "YOUR_GUILD_INVITE_LINK"
    MONGO_TOKEN= "YOUR_MONGO_DB_TOKEN"
    API_KEY= 'YOUR_API_KEY'
    OWNER_ID = "YOUR_OWNER_USER_ID"
    STATUS_PAGE = 'https://huskybot1.statuspage.io/'
    BOT_INVITE_LINK = 'YOUR_BOT_INVITE_LINK'
    BUG_REPORT_CHANNEL_ID = 'YOUR_BUG_REPORT_CHANNEL_ID'
    BOT_STATUS_CHANNEL_ID = "YOUR_STATUS_CHANNEL_ID"
    BOT_ID = 'YOUR_BOT_ID'

6. **Customize and Enjoy**

    Customize your bot's behavior and commands as needed. Refer to the README and documentation for more details on configuring and using Husky.

    That's it! Husky bot should now be installed and ready to use on your server.
</details>
<br>

## Contributing

Contributions are welcomed to Husky! If you have ideas for improvements or want to report issues, please [open an issue](https://github.com/Laernos/Husky/issues) or submit a pull request.
<br><br>

## License

Husky is licensed under the [MIT](LICENSE). If you plan to use any part of this source code in your own bot, please include appropriate credit.

<br>

> [!WARNING]
> Just a friendly reminder that while Husky Bot comes packed with cool features, I haven't had the chance to do a full-on security check. So, you might want to take a look under the hood to ensure everything is functioning as it should.
