function change()
{

	//document.getElementById("mchart").src="https://books.google.com/ngrams/interactive_chart?content=Albert+Einstein%2CSherlock+Holmes&year_start=1800&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2CAlbert%20Einstein%3B%2Cc0%3B.t1%3B%2CSherlock%20Holmes%3B%2Cc0";
	var new_url="https://books.google.com/ngrams/interactive_chart?content=";
	var raw_keywords=document.getElementById('keywords').value;
	var keywords=new Array();
	if(-1==raw_keywords.indexOf(',')&& -1==raw_keywords.indexOf('，'))
		keywords[0]=raw_keywords;
	else
	{
		if(raw_keywords.indexOf(',')!=-1)
		{
			keywords=raw_keywords.split(',');		
		}
		if(raw_keywords.indexOf('，')!=-1)
		{
			keywords=raw_keywords.split('，');	
		}
	}
	if(escape(str).indexOf("%u")!=-1) //有汉字
	{
		
	}	
	else
	{
		
	}
	for(var i=0;i