import requests
class client_library(object):
	def __init__(self,access_token):
		self.access_token=access_token
		raw_out=""
		self.Address="https://api-ssl.bitly.com"
		self.new_link_dict={}
		self.history_dict={}
		self.click_dict={}
	
	def set_token(self,access_token):
		self.access_token=access_token
	
	
	
	def save_link(self,longUrl, title=None, note=None, private=None, user_ts=None,domain=None):		
		get_save="/v3/user/link_save?access_token="+self.access_token+"&longUrl="+longUrl		
		if title:
			get_save+="&title=%s" %(title)
		if note:
			get_save+="&note=%s" %(note)
		if private:
			get_save+="&private=%s" %(private)
		if user_ts:
			get_save+="&user_ts=%s" %(user_ts)
		if domain:
			get_save+="&domain=%s" %(domain)
		
		link=self.Address+get_save
		raw_out=None
		raw_out=requests.get(link,timeout=1)
		if not raw_out: return raw_out
		str_out=str(raw_out.text).replace('u\'','\'').replace('false','False').replace('true','True').replace('null','None')
		self.new_link_dict=eval(str_out)
		return raw_out
	
	
	def link_history(self, limit=None, offset=None, created_before=None, created_after=None, modified_after=None, expand_client_id=None, archived_optional=None, private_optional=None, user=None, exact_domain=None, root_domain=None, keyword=None, campaign_id=None, query=None):
		get_history="/v3/user/link_history?access_token="+self.access_token
		if limit:
			get_history+="&limit=%s" %(limit)
		if offset:
			get_history+="&offset=%s" %(offset)
		if created_before:
			get_history+="&created_before=%s" %(created_before)
		if created_after:
			get_history+="&created_after=%s" %(created_after)
		if modified_after:
			get_history+="&modified_after=%s" %(modified_after)
		if expand_client_id:
			get_history+="&expand_client_id=%s" %(expand_client_id)
		if archived_optional:
			get_history+="&archived optional=%s" %(archived_optional)
		if private_optional:
			get_history+="&private-optional=%s" %(private_optional)
		if user:
			get_history+="&user=%s" %(user)
		if exact_domain:
			get_history+="&exact_domain=%s" %(exact_domain)
		if root_domain:
			get_history+="&root_domain=%s" %(root_domain)
		if keyword:
			get_history+="&keyword=%s" %(keyword)	
		if campaign_id:
			get_history+="&campaign_id=%s" %(campaign_id)	
		if query:
			get_history+="&query=%s" %(query)
		
		link=self.Address+get_history
		raw_out=None
		raw_out=requests.get(link,timeout=1)
		if not raw_out: return raw_out
		str_out=str(raw_out.text).replace('u\'','\'').replace('false','False').replace('true','True').replace('null','None')
		self.history_dict=eval(str_out)
		return raw_out
	
	
	def link_click(self,unit=None,units=None,timezone=None,rollup=None,limit=None,unit_reference_ts=None,format=None):
		get_click="/v3/user/clicks?access_token="+self.access_token
		if unit:
			get_click+="&unit=%s" %(unit)
		if units:
			get_click+="&units=%s" %(units)
		if timezone:
			get_click+="&timezone=%s" %(timezone)
		if rollup:
			get_click+="&rollup=%s" %(rollup)
		if limit:
			get_click+="&limit=%s" %(limit)
		if unit_reference_ts:
			get_click+="&unit_reference_ts=%s" %(unit_reference_ts)
		if format:
			get_click+="&format=%s" %(format)
		
		link=self.Address+get_click
		raw_out=None
		raw_out=requests.get(link,timeout=1)
		if not raw_out: return raw_out
		str_out=str(raw_out.text).replace('u\'','\'').replace('false','False').replace('true','True').replace('null','None')
		self.click_dict=eval(str_out)
		return raw_out
		
	
	def get_latest_saved_longUrl(self):
		return self.new_link_dict['data']['link_save']['long_url']
	
	def get_latest_saved_aggregate_link(self):
		return self.new_link_dict['data']['link_save']['aggregate_link']
	
	def get_latest_saved_link(self):
		return self.new_link_dict['data']['link_save']['link']
	
	def get_all_link_history(self):
		self.link_history()
		return self.history_dict['data']['link_history']
	
	def get_all_clicks(self):
		self.link_click()
		return self.click_dict['data']['clicks']
	
	def get_all_links(self):
		links=[];
		self.link_history()
		history_dict=self.history_dict
		for i in history_dict['data']['link_history']:
			links=links+[i['link']]
		return links;
	
	def get_all_aggregate_links(self):
		links=[];
		self.link_history()
		history_dict=self.history_dict
		for i in history_dict['data']['link_history']:
			links=links+[i['aggregate_link']]
		return links;
	
	def get_all_longUrl(self):
		links=[];
		self.link_history()
		history_dict=self.history_dict
		for i in history_dict['data']['link_history']:
			links=links+[i['long_url']]
		return links;
		
	def most_click_day(self):
		return max(self.get_all_clicks())