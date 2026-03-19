/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pre.test.projects;

/**
 *
 * @author matth
 */
public class AreaCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int radius = 5;
        System.out.println(calculateArea(radius));
    }
    public static int calculateArea(int radius){
       return (int) (Math.PI * Math.pow(radius, 2));
    }
    
}
