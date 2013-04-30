<?PHP

function digital_root($n)
{
   return array_sum(str_split($n));
}

$input = $output = $argv[1];
while( $output > 9 )
  $output = digital_root($output);

echo "The digital root of $input is $output \n";
?>
