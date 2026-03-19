/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pre.test.projects;

import java.util.Scanner;

/**
 *
 * @author matth
 */
public class ReverseWord {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter in a word!");
        String word = keyboard.next();
        reverseString(word);
    }
    public static void reverseString(String word){
        String reversedWord = "";
        for(int i = word.length()-1; i >=0; i--){
            reversedWord += word.charAt(i);
        }
        System.out.println(reversedWord); 
        printLetters(reversedWord);
    }
    public static void printLetters(String reversedWord){
        System.out.println("Reversed word with every 2nd letter printed");
        for(int i = 0; i<reversedWord.length(); i++){
            if(i%2 == 0){
                System.out.print(reversedWord.charAt(i));
            }
        }
    }
    
}
