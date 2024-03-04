full_size_x = 10000;
full_size_y = 15000;
full_size_z = 36;
x_max = 30-1;
y_max = 26-1;
z_max = 10-1;

hold on;

data = csvread('cropped_coords.csv');
x = data(:, 1); % Extracts the first column
y = data(:, 2); % Extracts the second column
z = data(:, 3); % Extracts the third column

x = x*full_size_x/x_max;
y = y*full_size_y/y_max;
z = z*full_size_z/z_max;

% Not quite what we want
% plot(x, y);
% xlabel('x'); % Label for x-axis
% ylabel('y'); % Label for y-axis
% title('2D Plot of x vs. y'); % Title of the plot

% Scatter
% scatter3(x, y, z);
% xlabel('x'); % Label for x-axis
% ylabel('y'); % Label for y-axis
% zlabel('z'); % Label for z-axis
% title('3D Scatter Plot of x, y, z'); % Title of the plot

% Failed to create surface
% surf(x, y, z); % Creates the surface plot
% xlabel('x');
% ylabel('y');
% zlabel('z');
% title('Surface Plot');

% Surface with average
% uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
% aggregatedZ = arrayfun(@(i) mean(z(all([x, y] == uniqueXY(i,:), 2))), 1:size(uniqueXY, 1));
% % Now you can plot aggregatedZ against the unique (x, y) pairs
% [xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
% zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
% surf(xq, yq, zq); % Plot

% 3D scatter with colors
% scatter3(x, y, z, 5, z, 'filled'); % The '5' sets the marker size, and 'z' sets the color
% xlabel('x');
% ylabel('y');
% zlabel('z');
% title('3D Scatter Plot Showing Multiple z Values for Each (x, y)');
% colorbar; % Adds a color bar to interpret the colors

% Contour with average
uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
aggregatedZ = arrayfun(@(i) mean(z(all([x, y] == uniqueXY(i,:), 2))), 1:size(uniqueXY, 1));
% Now you can plot aggregatedZ against the unique (x, y) pairs
[xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
contourf(xq, yq, zq); % Creates a filled contour plot
colorbar; % Shows the scale of values

% Contour with average improved
% % Assuming x, y, and z are column vectors of the same length
% uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
% % Preallocate aggregatedZ for efficiency
% aggregatedZ = zeros(size(uniqueXY, 1), 1);
% % Iterate over each unique (x, y) pair to find and average corresponding z values
% for i = 1:size(uniqueXY, 1)
%     mask = x == uniqueXY(i,1) & y == uniqueXY(i,2); % Logical index for matching (x, y) pairs
%     aggregatedZ(i) = mean(z(mask)); % Average z values for the current unique (x, y) pair
% end
% % Continue with grid and interpolation as before
% [xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
% zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
% contourf(xq, yq, zq); % Creates a filled contour plot
% colorbar; % Shows the scale of values

% Contour with average improved 2
% % Assuming x, y, and z are column vectors of the same length
% uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
% % Preallocate aggregatedZ for efficiency
% aggregatedZ = zeros(size(uniqueXY, 1), 1);
% % Iterate over each unique (x, y) pair to find and average corresponding z values
% for i = 1:size(uniqueXY, 1)
%     mask = x == uniqueXY(i,1) & y == uniqueXY(i,2); % Logical index for matching (x, y) pairs
%     aggregatedZ(i) = mean(z(mask)); % Average z values for the current unique (x, y) pair
% end
% % Continue with grid and interpolation as before
% [xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
% zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
% % After calculating zq with griddata
% mask = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq, 'nearest'); % Interpolate but keep 'nearest' for masking
% zq(isnan(mask)) = NaN; % Set zq to NaN where mask is NaN (i.e., no nearby original data points)
% % Now, plotting with NaNs in zq will leave gaps in the contour plot
% contourf(xq, yq, zq); % Creates a filled contour plot with gaps
% colorbar; % Shows the scale of values

% Mesh plot with average
% uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
% aggregatedZ = arrayfun(@(i) mean(z(all([x, y] == uniqueXY(i,:), 2))), 1:size(uniqueXY, 1));
% % Now you can plot aggregatedZ against the unique (x, y) pairs
% [xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
% zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
% mesh(xq, yq, zq); % X, Y, and Z should be matrices
% xlabel('x'), ylabel('y'), zlabel('z');
% title('Mesh Plot');

% Waterfall with average
% uniqueXY = unique([x, y], 'rows'); % Find unique (x, y) pairs
% aggregatedZ = arrayfun(@(i) mean(z(all([x, y] == uniqueXY(i,:), 2))), 1:size(uniqueXY, 1));
% % Now you can plot aggregatedZ against the unique (x, y) pairs
% [xq, yq] = meshgrid(linspace(min(x), max(x), 100), linspace(min(y), max(y), 100)); % Create a grid
% zq = griddata(uniqueXY(:,1), uniqueXY(:,2), aggregatedZ, xq, yq); % Interpolate z values on the grid
% waterfall(xq, yq, zq);
% xlabel('x'), ylabel('y'), zlabel('z');
% title('Waterfall Plot');

hold off;