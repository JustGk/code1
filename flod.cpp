#include <graphics.h>
#include <conio.h>
void ffill(int x, int y, int n, int o){
	int current=getpixel(x,y);
	if(current==o){
		putpixel(x,y,n);
//		delay(10);
		ffill(x,y+1,n,o);
		ffill(x,y-1,n,o);
		ffill(x-1,y,n,o);
		ffill(x+1,y,n,o);
		ffill(x-1,y-1,n,o);
		ffill(x-1,y+1,n,o);
		ffill(x+1,y-1,n,o);
		ffill(x+1,y+1,n,o);
		
		
	}
}
void dl(int x1,int y1,int x2,int y2){
	float x, y,dx,dy,steps,xinc,yinc;
    dx = (x2-x1);
    dy=(y2-y1);
    setlinestyle(1,3,3);
    if(abs(dx)>abs(dy))
           {
        steps = dx;
    }
    else
           {
        steps = dy;
    }
    xinc = dx/steps;
    yinc = dy/steps;
    x = x1;
    y = y1;
    int i = 1;
    putpixel(x,y,BLACK);
    while(i<= steps)
    {
        
        x += xinc;
        y += yinc;
        putpixel(x,y, BLACK);
        i=i+1;
//      	delay(0.9);
    }
}
int main()
{
    int gd = DETECT ,gm;
    
    initgraph(&gd, &gm, "");    
    setbkcolor(15);
    cleardevice();
    dl(50,50,250,50);
    dl(50,50,50,250);
    dl(100,50,100,250);
    dl(150,50,150,250);
    dl(200,50,200,250);
    dl(50,250,250,250);
    dl(50,200,250,200);
    dl(50,150,250,150);
    dl(50,100,250,100);
    dl(250,50,250,250);
    ffill(105,55,0,15);
    ffill(105,55,0,15);
    ffill(205,55,0,15);
    ffill(55,105,0,15);
    ffill(205,55,0,15);
    ffill(105,155,0,15);
    ffill(155,205,0,15);
	ffill(155,105,0,15);
	ffill(55,205,0,15);
	ffill(205,155,0,15);
    getch();
    closegraph();
}
