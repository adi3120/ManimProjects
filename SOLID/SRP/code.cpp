class Fazen
{
protected:
	HANDLE outhnd;
	HANDLE inhnd;
	SMALL_RECT rect_win;
	CHAR_INFO *buffscreen = new CHAR_INFO[s_width * s_height];
	COORD characterPos = {0, 0};
	COORD buffersize = {short(s_width), short(s_height)};
	float center_x = 0;
	float center_y = 0;
	float tempCenterx;
	float tempCentery;
	int consoleRangeStartx;
	int consoleRangeStarty;
	POINT p;
	int fontH;
	int fontW;

public:
	Fazen(){
		outhnd = GetStdHandle(STD_OUTPUT_HANDLE);
		inhnd = GetStdHandle(STD_INPUT_HANDLE);
		rect_win = {0, 0, (short)(s_width - 1), short(s_height - 1)};
		// Enable the window and mouse input events.
	}
	void push(){
		tempCenterx = center_x;
		tempCentery = center_y;
	}
	void pop(){
		center_x = tempCenterx;
		center_y = tempCentery;
	}
	float mapBounds(float value, float x1, float x2, float y1, float y2){
		float m = (y2 - y1) / (x2 - x1);
		float b = y1 - m * x1;
		value = (value - b) / m;
		return value;
	}
	void GetWindowPos(){
		int x;
		int y;
		RECT rect = {};
		GetWindowRect(GetConsoleWindow(), &rect);
		x = rect.left;
		y = rect.top;
		consoleRangeStartx = x;
		consoleRangeStarty = y;
	}
	float Mouse_X(){
		GetCursorPos(&p);
		GetWindowPos();
		p.x = mapBounds(p.x, 0, s_width, consoleRangeStartx, consoleRangeStartx + (s_width - 1) * fontW);
		return p.x;
	}
	float Mouse_Y(){
		GetCursorPos(&p);
		GetWindowPos();
		p.y = mapBounds(p.y, 0, s_height, consoleRangeStarty, consoleRangeStarty + (s_height - 1) * fontH);
		return p.y - 3;
	}
	const void display(){
		WriteConsoleOutputW(outhnd, buffscreen, buffersize, characterPos, &rect_win);
	}
	const void background(short col = 0){
		for (int i = 0; i < s_height * s_width; i++){
			buffscreen[i].Char.UnicodeChar = ' ';
			buffscreen[i].Attributes = col;
		}
	}
	const void Plot(float x, float y, short col = whiteF, short c = 0x2588){
		QUICKTRANSLATE
		if (x > 1 && x < s_width - 1 && y > 1 && y < s_height - 1){
			buffscreen[int(x) + s_width * int(y)].Char.UnicodeChar = c;
			buffscreen[int(x) + s_width * int(y)].Attributes = col;
		}
	}
	void drawLine(float x2, float y2, float x1, float y1, short col = whiteF, short c = 0x2588){
		float x, y, dx, dy, dx1, dy1, px, py, xe, ye, i;
		dx = x2 - x1;
		dy = y2 - y1;
		dx1 = std::abs(dx);
		dy1 = std::abs(dy);
		px = 2 * dy1 - dx1;
		py = 2 * dx1 - dy1;
		if (dy1 <= dx1){
			if (dx >= 0){
				x = x1;
				y = y1;
				xe = x2;
			}
			else{
				x = x2;
				y = y2;
				xe = x1;
			}
			Plot(x, y, col, c);
			for (i = 0; x < xe; i++){
				x = x + 1;
				if (px < 0)
					px = px + 2 * dy1;
				else{
					if ((dx < 0 && dy < 0) || (dx > 0 && dy > 0))
						y = y + 1;
					else
						y = y - 1;
					px = px + 2 * (dy1 - dx1);
				}
				Plot(x, y, col, c);
			}
		}
		else{
			if (dy >= 0){
				x = x1;
				y = y1;
				ye = y2;
			}
			else{
				x = x2;
				y = y2;
				ye = y1;
			}
			Plot(x, y, col, c);
			for (i = 0; y < ye; i++){
				y = y + 1;
				if (py <= 0)
					py = py + 2 * dx1;
				else{
					if ((dx < 0 && dy < 0) || (dx > 0 && dy > 0))
						x = x + 1;
					else
						x = x - 1;
					py = py + 2 * (dx1 - dy1);
				}
				Plot(x, y, col, c);
			}
		}
	}

	void translate(float x, float y){
		center_x = x;
		center_y = y;
	}

	const void drawTextFromInt(int x, int y, wstring s, int b, short col = whiteF){
		QUICKTRANSLATE
		std::wostringstream ws;
		ws << b;

		std::wstring a = s + (ws.str());

		for (size_t i = 0; i < a.size(); i++){
			buffscreen[x + i + s_width * y].Char.UnicodeChar = a[i];
			buffscreen[x + i + s_width * y].Attributes = col;
		}
	}
	const void Text(int x, int y, wstring a, short col = whiteF){
		QUICKTRANSLATE
		for (size_t i = 0; i < a.size(); i++){
			buffscreen[x + i + s_width * y].Char.UnicodeChar = a[i];
			buffscreen[x + i + s_width * y].Attributes = col;
		}
	}
};
