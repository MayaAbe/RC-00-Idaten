#RaspberryPi用のラジコン制御コード(製作2019年8月)
#キーボード接続による制御(Bluetooth推奨)


#必要なモジュールのインポート
import RPi.GPIO as GPIO #モータの回転方向と速度の制御
import wiringpi as pi  #サーボモータの回転角制御
import time

#変数の指定
FRONT_PIN = 23  #駆動系の前転
BACK_PIN = 24  #駆動系の後転
PWM_DUTY = 100  #PWMサイクルを指定
servo_pin = 18  #サーボの回転角を指定

#サーボ関係の諸々を設定
CYCLE = 20
MIN_PULSE = 0.5
MAX_PULSE = 2.4
MIN_DEG = 0
MAX_DEG = 180
RANGE = 2000

#GPIOのエラーメッセージを無効化
GPIO.setwarnings(False)

#ピン番号はBCMで指定
GPIO.setmode(GPIO.BCM)
#前転と後転のピンを起動
GPIO.setup(FRONT_PIN,GPIO.OUT)
GPIO.setup(BACK_PIN,GPIO.OUT)


#PWMはを0~100で指定
pwmout = GPIO.PWM(FRONT_PIN,100)


pwmout.start(0)


#ラジコンの操作系演算
while True:
    #テンキーからラジコンの速さ・ハンドルを受け取る
    speed_input = input('Input:')

    #int型以外で受け取ったらスルーする
    try:
        num = int(speed_input)
    except:
        pass
        print('ATTENTION:fill in number')
    speed = 0


    #0で停止、2で前進、22で加速、1で左折&3で右折
    if num==0:
        speed = 0
    elif num==2:
        speed =70
        set_degree = 120


        clock = int( 19.2 / float(RANGE) * CYCLE * 1000 )
        min_val = RANGE * MIN_PULSE / CYCLE
        max_val = RANGE * MAX_PULSE / CYCLE

        pi.wiringPiSetupGpio()
        pi.pinMode( servo_pin, pi.GPIO.PWM_OUTPUT )
        pi.pwmSetMode( pi.GPIO.PWM_MODE_MS )
        pi.pwmSetRange( RANGE )
        pi.pwmSetClock( clock )

        if ( set_degree <= MAX_DEG and set_degree >= MIN_DEG ):
            move_deg = int( ( max_val - min_val ) / MAX_DEG * set_degree )
            pi.pwmWrite( servo_pin, move_deg )

    elif num==22:
        speed = 100
    elif num==1:
        speed=70
        set_degree = 155

        clock = int( 19.2 / float(RANGE) * CYCLE * 1000 )
        min_val = RANGE * MIN_PULSE / CYCLE
        max_val = RANGE * MAX_PULSE / CYCLE

        pi.wiringPiSetupGpio()
        pi.pinMode( servo_pin, pi.GPIO.PWM_OUTPUT )
        pi.pwmSetMode( pi.GPIO.PWM_MODE_MS )
        pi.pwmSetRange( RANGE )
        pi.pwmSetClock( clock )

        if ( set_degree <= MAX_DEG and set_degree >= MIN_DEG ):
            move_deg = int( ( max_val - min_val ) / MAX_DEG * set_degree )
            pi.pwmWrite( servo_pin, move_deg )
    elif num==3:
        speed=70
        set_degree = 90

        clock = int( 19.2 / float(RANGE) * CYCLE * 1000 )
        min_val = RANGE * MIN_PULSE / CYCLE
        max_val = RANGE * MAX_PULSE / CYCLE

        pi.wiringPiSetupGpio()
        pi.pinMode( servo_pin, pi.GPIO.PWM_OUTPUT )
        pi.pwmSetMode( pi.GPIO.PWM_MODE_MS )
        pi.pwmSetRange( RANGE )
        pi.pwmSetClock( clock )

        if ( set_degree <= MAX_DEG and set_degree >= MIN_DEG ):
            move_deg = int( ( max_val - min_val ) / MAX_DEG * set_degree )
            pi.pwmWrite( servo_pin, move_deg )


    pwmout.ChangeDutyCycle(speed)



#使うことはないだろうけど終了操作
pwmout.stop
GPIO.cleanup()
