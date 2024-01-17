from libary import *
from main_parsing import chords_text, song_list
from keyboard import main_kb

Token = ''
bot = Bot(token=Token, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command (commands=['start']))
async def start_command(message: Message):
    await message.answer(f'<b> Привет {message.from_user.first_name}! </b>\n'
                         f'<b> Это бот по выводу аккордов! </b>\n'
                         f'<b> Ниже показаны все фунции этого бота! </b>',
                         reply_markup= main_kb)


@dp.message(Command(commands=['selectSong']))
async def find(message: Message, command: CommandObject):
    print(f'{message.from_user.first_name} - {command.args}', '\n' * 2)
    chords = ''
    if command.args == None:
        await message.reply('<b> Чтобы воспользоваться этой функцией напшите команду так: \n/selectSong название песни </b>')
    else:
        chords = chords_text(str(command.args))
        if chords == 'Такой песни увы не сущесвует :(':
            await message.reply('Такой песни увы не существует :(')
        else:
            x, y = 0, 800
            while y < len(chords):
                await message.answer(f'{chords[x:y]}')
                if (y + 800 >= len(chords) or x + 800 >= len(chords)):
                    x = y - x
                    y = len(chords) - 1
                    await message.answer(f'{chords[x:y]}')
                    break
                x, y = x + 800, y + 800

@dp.message(Command(commands=['findSong']))
async def find(message: Message, command: CommandObject):
    if command.args == None:
        await message.reply('<b> Чтобы воспользоваться этой функцией напшите команду так: \n/findSong название песни </b>')
    else:
        songs = song_list(str(command.args))
        if songs == 'Такой песни увы не сущесвует :(':
            await message.reply('Такой песни увы не существует :(')
        else:
            await message.answer(songs)


@dp.message(Command(commands=['creaters']))
async def find(message: Message, command: CommandObject):
    await message.reply('creator is @wakeupkstnv \n'
                        'Весь фидбек ему в личку!')

@dp.message(Command(commands=['help']))
async def find(message: Message, command: CommandObject):
    await message.reply('<b>/start</b> - для рестарта кнопок и функционала бота \n'
                        '<b>/findSong</b> - для поиска списка песни исполнителя \n'
                        '<b>/selectSong</b> - для выбора этой же песни')

@dp.message(Command(commands=['aboutBot']))
async def find(message: Message, command: CommandObject):
    await message.reply('beta version of bot v0.1')

@dp.message()
async def echo(message: Message):
    print(message.text)
    phras = ['Команда не распознана. Возможно, вы опечатались или используете неизвестный мне синтаксис.',
             'Извините, но я не знаком с такой командой. Возможно, вы хотели что-то другое?',
             'К сожалению, я не распознаю эту команду. Возможно, она не входит в мой набор инструкций.',
             'Извините, но я не понимаю вашей команды. Может быть, она относится к функционалу, который мне неизвестен.',
             ]
    await message.reply(f'{phras[randint(0, len(phras) - 1)]}')

async def main():
    await bot.delete_webhook(drop_pending_updates=True) # Остановка нон стоп спама
    await dp.start_polling(bot) # Чтобы бот работал нон-стопом

if __name__ == '__main__':
    asyncio.run(main())