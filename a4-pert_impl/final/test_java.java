class test_java{
    public static void main(String args[]){
        try{
            java.lang.Runtime rt = java.lang.Runtime.getRuntime();
           java.lang.Process p = rt.exec("python3 sample-gantt.py");
       }
       catch(Exception e){
           System.out.println(e);
       }
    }
}
