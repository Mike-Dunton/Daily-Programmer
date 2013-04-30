<?php

function aeiouy($lines)
{
  $words = array();
  foreach ($lines as $word)
  {
    preg_replace('/^aeiouy/', '', $word);
    echo "$word \n";
    if($word == 'aeiouy')  
      $words.append($word);
  }  
  return $words;
}
$lines = file($argv[1]);

print_r(aeiouy($lines));
