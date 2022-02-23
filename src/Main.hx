class Main {
	static function main() {
		trace("Starting program...");

		// detect if the file is javascript or python and indicate to user
		#if js
		trace("JavaScript mode");
		#elseif python
		trace("Python mode");
		#end

		// create a new variable with type defined
		var foo:Int = 69;
		// create a new variable with type assumed
		var bar = 420;
		// print both
		trace(foo);
		trace(bar);
	}
}
