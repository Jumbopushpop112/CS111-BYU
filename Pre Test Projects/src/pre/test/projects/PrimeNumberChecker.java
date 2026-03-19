/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pre.test.projects;

/**
 *
 * @author matth
 */
public class PrimeNumberChecker {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println(isPrime(8));
    }
    public static boolean isPrime(int num){
        if(num <= 1){
            return false;
        }
        for(int i = 2; i<num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }   
}
