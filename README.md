# hello_BlackJack
Python project #1 20181112

Read Me Please!
========================================================


1.	Project BlackJack 설명(What this project BlackJack  is all about.)
--------------------------------------------------------------------------------


도박장이나 인터넷게임에서 쉽게 접할 수 있는 블랙잭 게임을 파이썬의 class , 함수, 메서드, 클래스의 상속 및 외부모듈을 이용하여 코딩하였습니다. 이를 통해서  클래스와 메서드 그리고 외부모듈에 대한 이해를 높였습니다.
 
(Project BlackJack(PBJ) has been coded in Python using classes, functions, methods, objects and modules, which was able to get us familiar with these hard-to-crack conceptions. )


2.	Collaborators:
   ----------------------------------------------------------------------------------------
김주동, 엄희진, 백영래 ( Kim Joo-Dong, Eum Hee-Jin, Back Young-Rae)


3.	설치(What you need to install to run PBJ)
--------------------------------------------------------------------------------------


본 프로그램 실행을 위해서는 파이썬 3  IDE 를 설치할 필요가 있습니다.
설치방법은 다음 URL를 참조하세요. [Visual Studio Code Link]: https://code.visualstudio.com/Download
본인 컴퓨터의 OS에 따라서 적당한 버전을 선택해서 설치합니다. 


(Visual Studio Code(VSC) is recommended to be installed to run PBJ, not to mention installing the latest version Python3. For VSC installation, refer to the following URL [Visual Studio Code Link]: https://code.visualstudio.com/Download
Before you install IDE, choose the version that fits OS on your computer.)


4.	실행방법 (How to run PBJ)
--------------------------------------------------------------------------------------


비쥬얼 스튜디오 코드를 실행한 후에 entry point 인 main.py를 선택해서 run을  실행합니다.  게임이 실행되면 “Welcome to BlackJack” 이라는 메시지가 나오면서 딜러와 플레이어에게 각각 두 장씩 카드가 주어집니다.


 (After running VSC, you need to choose “ main.py “ and run it, which is an entry point for PBJ. If you initiate PBJ by running “ main.py “, “Welcome to BlackJack” pops up on your screen with two cards given to the player and the dealer each.) 


ACE는 11과 1로 둘 다 모두 쓸 수 있고, J, Q, K는 10으로 계산되며 두 카드의 수의 합이 21(ACE와 10의 카드 또는 J, Q, K)이되면 BlackJack이 되어서 이기게 됩니다. 만약  BlackJack이 아닐 경우 플레이와 딜러 중에서 21에 가장 근접한 사람이 이깁니다. 그리고 카드의 숫자의 합이 21을 넘어가게 되면 패합니다. 


(Aces may be counted as 1 or 11 points according to pip value, and tens and face cards count as ten points. The value of a hand is the sum of the point values of the individual cards. By the way,  a "blackjack" is the highest hand, consisting of an ace and any 10-point card. If you don’t have a blackjack, to beat the dealer, the player must to get as close to 21 as possible, without going over 21, outscoring the dealer or have the dealer bust.)


2장의 카드를 받고 나서, 합이 21이하면 플레이어는 Hit(H)와  Stay(S) 중에서 H를 눌러서 추가로 카드를 한 장 받을 수도 있고 S를 눌러서 딜러와 승패를 가를 수 있습니다. (After being dealt two cards summed up to less than 21 points, the player can either hit to get another card or stay to stand pat with his cards to see who’s got more points of the two. )


딜러는 카드의 수의 합이 17미만이면  카드를 더 받아야 합니다.  17이상이면 더 받을 필요가 없습니다.   은근 중독성 있는 게임입니다.  즐겜하세요.   Good Luck!   버그 발견시 태클 환영 합니다. ^^


(If the dealer has 16 or less, then he will draw another card. Just in case of more than 17, there’s no need to draw another card. Blackjack is so irresistible that you cannot quit. Have fun and good luck! If you find any glitch or bug during the play, feel free to contact us at larryback@naver.com)

