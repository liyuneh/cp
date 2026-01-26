public class Name{
    public static void main(String[] args){
        for (int i = 0; i < 5; i ++) {
            if (i == 2){
                break;
            } else if (i == 3){
                continue;
            } else if(i == 4){
                return;
            }
            System.out.println("Hello World " + i);
        
        }

    }
}