<?php
/*#############################################################################
*Find words in a word list that contain all the owels in alphabetical order
*non-repeated, where vowels are defined as A E I O U Y
*##############################################################################
*/

function aeiouy($lines)
{
  
  foreach ($lines as $word)
  {
		$vowelCheck = '';
		foreach(str_split($word) as $char)
		{
			if(in_array($char, str_split("aeiouy")))
			{
				$vowelCheck = $vowelCheck.$char;
			}
		}
		if(strtolower($vowelCheck) == "aeiouy")
		{
			echo $word;
		}
	}
}

$lines = file($argv[1]);
aeiouy($lines);

?>
