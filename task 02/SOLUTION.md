epicgeek11@LAPTOP-0S6IFQVO:/mnt/d$ mkdir Coordinates-Location #creating diretory coordinates location

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d$ cd Coordinates-Location #changing the current directory to coordinates location

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ mkdir North #creating new directory north

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ cd North #changing directory

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ touch NDegree.txt | echo "9°" >NDegree.txt #creating text files and adding value

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ touch NMinutes.txt | echo "5'">NMinutes.txt #creating text files and adding value

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ touch NSeconds.txt | echo "38.1\"">NSeconds.txt #creating text files and adding value

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ touch NorthCoordinate.txt | cat NDegree.txt  NMinutes.txt  NSeconds.txt >NorthCoordinate.txt #creating northcoordinate file

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ mv NorthCoordinate.txt  /mnt/d/Coordinates-Location/North.txt #moving northcoordinate.txt to north.txt

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/North$ cd /mnt/d/Coordinates-Location #changing current working directory

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ mkdir East #creating east directory

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ cd East #chanding current working directory

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ touch EDegree.txt | echo "76°">EDegree.txt #creating necessary text files

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ touch EMinutes.txt | echo "29'">EMinutes.txt #creating necessary text files

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ touch ESeconds.txt | echo "30.8\"">ESeconds.txt #creating necessary text files

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ touch EastCoordinate.txt | cat EDegree.txt EMinutes.txt ESeconds.txt > EastCoordinate.txt #creating eastcoordinate

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ mv EastCoordinate.txt /mnt/d/Coordinates-Location/East.txt #moving eastcoordinate to east

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location/East$ cd /mnt/d/Coordinates-Location #changing current working directory

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ cat North.txt East.txt>Location-Coordinate.txt #creating location coordinate 

epicgeek11@LAPTOP-0S6IFQVO:/mnt/d/Coordinates-Location$ touch SOLUTION.md #creating solution md file

This is the whole command which i used for creating directories. The final location is 9°05'38.1"N 76°29'30.8"E. If we put this in google maps we will get the required location whose screenshot has been provided in the folder