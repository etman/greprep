<vocab-list>
<div class="col-md-7">
	<div class="row vocab-listing-heading">
		<div class="col-md-2"><h4>Vocabulary</h4></div>
		<div class="col-md-9"><h4>Definition</h4></div>
	</div>
	<div class="row" each={ vocabs }>
		<div class="col-md-2">{ word }</div>
		<div class="col-md-9">{ definition }</div>
		<div class="col-md-1">
			<img src="/web/images/dictcom.png" class="icon_img" onclick={ parent.lookUpDictCom } />
		</div>
	</div>
</div>
<div class="col-md-5 vocab-def-block">
</div>
<style>
.icon_img {
	width: 25px;
	height: 25px;
}
.vocab-def-block {
	border-left-width: thin;
	border-left-style: dashed;
	border-left-color: blue;
}
.vocab-listing-heading {
	border-bottom-width: thin;
	border-bottom-style: dashed;
	border-bottom-color: gray;
}
</style>
<script>
	var self = this;
	self.vocabs = [];

	self.lookUpDictCom = function(e) {
		console.info("1", e.item);
		riot.mount(".vocab-def-block", "vocab-def", e.item);
	}

	$.get("/api/vocab", function(data) {
		self.vocabs.length = 0;
		for (var i = 0; i < data.length; i++)
			self.vocabs.push(data[i]);
		self.update();
	}, "json");
</script>
</vocab-list>