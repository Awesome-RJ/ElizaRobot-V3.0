#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from tg_bot import pbot as StellaCli

async def get_user_id(message):
    if (
        message.reply_to_message
        and not message.forward_from
    ):
        if (
            len(message.command) >= 2
        ):
            args = message.command[1]
            if (
                args.startswith('@')
                or (
                    args.isdigit()
                    and (
                        len(args) >= 5
                        or len(args) <=15
                    )
                )
            ):
                user_info = await StellaCli.get_users(
                    user_ids=args
                )
            else:
                user_info = message.reply_to_message.from_user
        else:
            user_info = message.reply_to_message.from_user
    elif message.forward_from:
        user_info = message.forward_from
    else:
        if not (
            len(message.command) >= 2
        ):
            await message.reply(
                "I don't know who you're talking about, you're going to need to specify a user...!"
            )
            return False

        user = message.command[1]
        user_info = await StellaCli.get_users(
            user_ids=user
        )

    return user_info  

def get_text(message):
    if message.reply_to_message:
        return ' '.join(message.command[2:]) if (
            len(message.command) >= 2
            and (
                message.command[1].startswith('@')
                or (
                        message.command[1].isdigit()
                        and (
                            len(message.command[1]) >= 5
                            or len(message.command[1]) <=15
                        )
                )
            )
        ) else ' '.join(message.command[1:])
    else:
        return ' '.join(message.command[2:])
