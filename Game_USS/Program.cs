using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks.Sources;
using System.Xml;

namespace Snake
{
    class Program
    {
        
        static void Main(string[] args)
        {
            int score = 0;
            int Speed = 100;
            Console.SetWindowSize(90, 25);

            Console.WriteLine("(White, Yellow, Blue)");
            Console.WriteLine("Enter colour theme: ");
            string colourname = Console.ReadLine();
            if (colourname is "White")
            {
                Console.ForegroundColor = ConsoleColor.White;
            }
            else if (colourname is "Yellow")
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
            }
            else if (colourname is "Blue")
            {
                Console.ForegroundColor = ConsoleColor.Blue;
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.White;
            }
            Console.Clear();

            Console.WriteLine("Enter your name: ");
            string username = Console.ReadLine();
            Console.Clear();

            Walls walls = new Walls(80, 25);
            walls.Draw();

            // Отрисовка точек			
            Point p = new Point(4, 5, '*');
            Snake snake = new Snake(p, 4, Direction.RIGHT);
            snake.Draw();

            FoodCreator foodCreator = new FoodCreator(80, 25, '$');
            Point food = foodCreator.CreateFood();
            food.Draw();

            while (true)
            {
                Console.SetCursorPosition(Console.WindowWidth - 10, 1);
                Console.Write("Score:"+score);
                if (walls.IsHit(snake) || snake.IsHitTail())
                {
                    break;
                }
                if (snake.Eat(food))
                {
                    food = foodCreator.CreateFood();
                    food.Draw();
                    score++;
                    Speed -= 5;
                }
                else
                {
                    snake.Move();
                }
                Thread.Sleep(Speed);
                if (Console.KeyAvailable)
                {
                    ConsoleKeyInfo key = Console.ReadKey();
                    snake.HandleKey(key.Key);
                }
            }
            File.AppendAllText(@"C:\Users\M0RGAN\source\repos\Martin_Nommiste_TARpv22\Game_USS\result.txt", username+" "+score + Environment.NewLine);
            WriteGameOver();
            Console.ReadLine();
        }


        static void WriteGameOver()
        {
            int xOffset = 25;
            int yOffset = 8;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.SetCursorPosition(xOffset, yOffset++);
            WriteText("============================", xOffset, yOffset++);
            WriteText("     Mäng on lõpetanud", xOffset + 1, yOffset++);
            yOffset++;
            WriteText("============================", xOffset, yOffset++);
        }

        static void WriteText(String text, int xOffset, int yOffset)
        {
            Console.SetCursorPosition(xOffset, yOffset);
            Console.WriteLine(text);
        }

    }
}