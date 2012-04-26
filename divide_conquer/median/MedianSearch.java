
public class MedianSearch {

    private int numElements = 0;
    private Database database1 = null;
    private Database database2 = null;

    MedianSearch( int numElements ) {
        this.numElements = numElements;
        database1 = Database.getDatabase1();
        database2 = Database.getDatabase2();
    }

    Integer findMedian() {
        Integer median = Integer.MAX_VALUE;

        int index1 = (int)Math.ceil( numElements / 2.0 );
        int index2 = numElements - index1;
        boolean keepGoing = true;
        int stepSize = Math.min( index1, index2 );

        while( keepGoing ) {
            if( stepSize == 1 ) {
                keepGoing = false;
            }
            stepSize = (int) Math.ceil(stepSize / 2.0);
            Integer element1 = database1.getKthLargestValue( index1 );
            Integer element2 = database2.getKthLargestValue( index2 );

            System.out.print( "DB1[" + index1 + "] is " + element1 );
            System.out.println( ", DB2[" + index2 + "] is " + element2 );

            if( element1.compareTo( element2 ) < 0 ) {
                index1 = index1 + stepSize;
                index2 = numElements - index1;
                if( element2 < median ) {
                    median = element2;
                }
            } else {
                index2 = index2 + stepSize;
                index1 = numElements - index2;
                if( element1 < median ) {
                    median = element1;
                }
            }
        }

        return median;
    }

    Integer findMedianOld() {
        Integer median = Integer.MAX_VALUE;

        int index1 = (int)Math.ceil( numElements / 2.0 );
        int index2 = numElements - index1;
        float stepSize = Math.min( index1, index2 );

        while( stepSize >= 0.5 ) {
            stepSize = stepSize / 2;
            Integer element1 = database1.getKthLargestValue( index1 );
            Integer element2 = database2.getKthLargestValue( index2 );

            System.out.print( "DB1[" + index1 + "] is " + element1 );
            System.out.println( ", DB2[" + index2 + "] is " + element2 );

            int intStepSize = (int)Math.ceil(stepSize);
            if( element1.compareTo( element2 ) < 0 ) {
                index1 = index1 + intStepSize;
                index2 = numElements - index1;
                if( element2 < median ) {
                    median = element2;
                }
            } else {
                index2 = index2 + intStepSize;
                index1 = numElements - index2;
                if( element1 < median ) {
                    median = element1;
                }
            }
        }

        return median;
    }

    public static void main(String[] args) {
        int numElements = Database.DEFAULT_SIZE;
        if( args.length > 0 ) {
            numElements = Integer.parseInt( args[0] );
        }
        Database.Initialize(numElements);
        MedianSearch hw1 = new MedianSearch( numElements );
        Integer median = hw1.findMedian();
        System.out.println( "The algorithm returned " + median );
    }

}
