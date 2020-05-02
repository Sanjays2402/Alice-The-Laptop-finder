response = Map();
response.put("action","context");
response.put("context_id",context_id);
if(context_id.equals("browsing"))
{
	browsing = answers.get("browsing").get("text");
	if(browsing.equalsIgnoreCase("I'll search laptop myself from your site"))
	{
		response.put("action","context");
		response.put("context_id","browsing");
		question = {"name":"browsing","replies":{" [Click Here to find](http://lapguru.zohosites.com/laptop-buying-guide)"},"suggestions":{"Thanks"}};
		//question=("name":"browsing","replies":{{"type":"links","text":"Here are the references","image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRq8r4gy6Py902JqzQIqLAKEp7QpdAGmWfB01m7M__Z2trUER3f2RW8J9QpBBxlEj3YlCrOuAdKZPE&usqp=CAc","links":{{"url":"https://facebook.com","text":"Lapguru-home"}}}});
		response.put("questions",{question});
	}
	else if(browsing.equalsIgnoreCase("Let Alice find Laptop for me"))
	{
		//response = Map();
		response.put("action","context");
		response.put("context_id","browsing");
		//response.put("replies","Select the specificaltion that you need");
		question = {"name":"discount","replies":{"Thats fine.. I'll assist you. What is your budget ?"},"input":{"type":"slider","values":{"60k","70k","80k","90k","100k"}}};
		response.put("questions",{question});
	}
	else if(browsing.equalsIgnoreCase("6k"))
	{
		//response = Map();
		response.put("action","context");
		response.put("action","reply");
		response.put("replies",{"Hold on..."});
	}
	else if(browsing.equalsIgnoreCase("Chat again with Alice"))
	{
		response = Map();
		response.put("action","reply");
		response.put("replies",{"Looking for anything specific?"});
		response.put("suggestions",{"I'm new here, just searching for Laptops","I'm an existing 			laptop user and need help","I want to speak with Customer Executive"});
		return response;
	}
	else
	{
		response.put("action","reply");
		response.put("replies",{"What else can I help you with?"});
		response.put("suggestions",{"Chat again with Alice","I want to speak with Customer Executive"});
	}
}
else if(context_id.equals("help"))
{
	help = answers.get("help").get("text");
	if(help.equalsIgnoreCase("Questions about the product"))
	{
		response = Map();
		response.put("action","reply");
		response.put("replies",{"Is it a kind of Issue ?"});
	}
	else if(help.equalsIgnoreCase("I wanna upgrade my machine"))
	{
		response = Map();
		response.put("action","reply");
		response.put("replies",{"Sure, I'll help you to upgrade"});
		response.put("replies",{"For purpose you use PC ?"});
		response.put("input",{"type":"select","options":{"Gaming Purpose","Professional/Bussiness Usage","Casual Usage"}});
	}
	else if(help.equalsIgnoreCase("Can't find what I'm looking for"))
	{
		response = Map();
		response.put("action","forward");
		response.put("action","reply");
		response.put("replies",{"Sorry that I can't help you properly.","Hold on. I'm Connecting you to support team"});
		return response;
	}
	else if(help.startsWith("hi"))
	{
		response = Map();
		response.put("action","reply");
		response.put("replies","Hi ! how are you ?");
	}
	else
	{
		question = {"name":"need","replies":{"What do you need help with?"},"suggestions":{"Regarding Warrenty and Claim","Specification clarification","Can't find what I'm looking for"}};
		response.put("questions",{question});
	}
}
else if(context_id.equals("demo"))
{
	time = answers.get("time").get("text");
	if(!answers.containsKey("email"))
	{
		question = {"name":"email","replies":{{"text":"Do you have an email address where we can reach you?","field_name":"siq_email","validate":{"format":"email","error":{"Enter a valid email"}}}}};
		response.put("questions",{question});
	}
	else
	{
		email = answers.get("email").get("text");
		response.put("action","end");
		response.put("replies",{"Thanks! One of our product specialists will reach out to you soon."});
	}
}
return response;
